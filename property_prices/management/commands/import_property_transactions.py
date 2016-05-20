import uuid
import pandas

from django.core.management.base import BaseCommand, CommandError

from property_prices.models import Property, Transaction


class Command(BaseCommand):

    help = "Imports the U.K Land Registry's Price Paid Data"

    def handle(self, *args, **options):
        # TODO: The following hard-coded file paths should be an
        # externally-specified argument
        postcode_locations = pandas.read_csv('NSPL_FEB_2016_UK.csv').set_index('pcds')
        property_transactions = pandas.read_csv('pp-complete.csv',
                                          header=None,
                                          names=[
                                              'transaction_id',
                                              'transaction_price',
                                              'transaction_transfer_date',
                                              'property_postcode',
                                              'property_type',
                                              'property_age',
                                              'property_duration',
                                              'property_paon',
                                              'property_saon',
                                              'property_street',
                                              'property_locality',
                                              'property_town_or_city',
                                              'property_district',
                                              'property_county',
                                              'transaction_category',
                                              '_record_type'
                                          ]).fillna('')

        property_transactions_grouped = property_transactions.groupby([
                                   'property_saon',
                                   'property_paon',
                                   'property_street',
                                   'property_town_or_city',
                                   'property_postcode',
                                   'property_district',
                                   'property_county'])

        for property, transactions in property_transactions_grouped:
            p = Property.objects.create(
                saon=property[0],
                paon=property[1],
                street=property[2],
                town_or_city=property[3],
                postcode=property[4],
                district=property[5],
                county=property[6],
            )

            try:
                p.latitude=postcode_locations['lat'][property[4]]
                p.longitude=postcode_locations['long'][property[4]]
                p.save()
            except KeyError:
                self.stdout.write(self.style.ERROR("Couldn't geocode postcode: %s" % p.postcode))

            for transaction in transactions.iterrows():
                # CHECK: I think the following implicitly relies on
                # the incoming data being sorted by date, which it is.
                if not p.locality:
                    p.locality = transaction[1]['property_locality']
                p.type = transaction[1]['property_type']
                p.age = transaction[1]['property_age']
                p.duration = transaction[1]['property_duration']
                p.save()
                t = Transaction.objects.create(
                    id=uuid.UUID(transaction[1]['transaction_id']),
                    property=p,
                    price = transaction[1]['transaction_price'],
                    category = transaction[1]['transaction_category'],
                    transfer_date = transaction[1]['transaction_transfer_date'].replace(' 00:00', ''))

            self.stdout.write(self.style.SUCCESS('Processed transaction %s' % t.id))

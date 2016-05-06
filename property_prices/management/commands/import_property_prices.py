import uuid
import pandas

from django.core.management.base import BaseCommand, CommandError

from property_prices.models import Property, Transaction


class Command(BaseCommand):

    help = "Imports the U.K Land Registry's Price Paid Data"

    def handle(self, *args, **options):
        # TODO: The following hard-coded file path should be an
        # externally-specified argument
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
                                   'property_locality',
                                   'property_town_or_city',
                                   'property_postcode',
                                   'property_district',
                                   'property_county'])

        for property, transactions in property_transactions_grouped:
            p = Property.objects.create(
                saon=property[0],
                paon=property[1],
                street=property[2],
                locality=property[3],
                town_or_city=property[4],
                postcode=property[5],
                district=property[6],
                county=property[7],
            )

            for transaction in transactions.iterrows():
                t = Transaction.objects.create(
                    id=uuid.UUID(transaction[1]['transaction_id']),
                    property=p,
                    price = transaction[1]['transaction_price'],
                    category = transaction[1]['transaction_category'],
                    transfer_date = transaction[1]['transaction_transfer_date'].rstrip(' 00:00'))

            # TODO: Sort the transactions in ascending order by
            # transaction_transfer_date and set the following in
            # 'p' for the last transaction?
            # type=row['property_type'],
            # age=row['property_age'],
            # duration=row['property_duration'],

            self.stdout.write(self.style.SUCCESS('Processed transaction %s' % t.id))

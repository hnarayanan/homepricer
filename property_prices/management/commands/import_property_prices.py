import uuid
import pandas

from django.core.management.base import BaseCommand, CommandError

from property_prices.models import Property, Transaction


class Command(BaseCommand):

    help = "Imports the U.K Land Registry's Price Paid Data"

    def handle(self, *args, **options):
        # TODO: The following hard-coded file path should be an
        # externally-specified argument
        property_prices = pandas.read_csv('pp-complete.csv',
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

        for index, row in property_prices.iterrows():
            property, _ = Property.objects.get_or_create(
                postcode=row['property_postcode'],
                type=row['property_type'],
                age=row['property_age'],
                duration=row['property_duration'],
                paon=row['property_paon'],
                saon=row['property_saon'],
                street=row['property_street'],
                locality=row['property_locality'],
                town_or_city=row['property_town_or_city'],
                district=row['property_district'],
                county=row['property_county'],
            )
            transaction, created = Transaction.objects.get_or_create(
                id=uuid.UUID(row['transaction_id']),
            )
            if created:
                transaction.property = property
                transaction.price = row['transaction_price']
                transaction.category = row['transaction_category']
                transaction.transfer_date = row['transaction_transfer_date'].rstrip(' 00:00')
                transaction.save()

            self.stdout.write(self.style.SUCCESS('Processed transaction %s' % transaction.id))

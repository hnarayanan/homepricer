from django.core.management.base import BaseCommand

from property_prices.models import Transaction


class Command(BaseCommand):

    help = "Export the average prices over time for rendering a choropleth"

    def add_arguments(self, parser):
        parser.add_argument('years', nargs='+', type=str)

    def handle(self, *args, **options):
        years = options['years']
        for year in years:
            transactions = Transaction.objects.filter(transfer_date__year=year).count()
            self.stdout.write(self.style.SUCCESS('{transactions} transactions in {year}'.format(transactions=transactions, year=year)))





# ----------------------
# NOTE: YEARLY TRANSACTIONS
# from property_prices.models import Property, Transaction

# for year in range(1995, 2016 + 1):
#     print year, ",",
#     for property_type in Property.TYPES:
#         print Transaction.objects.filter(transfer_date__year=year,
#                                          property__type=property_type[0]).count(), ",",
#     print


        # Export postcode geocodes
                # postcode_locations = pandas.read_csv('NSPL_FEB_2016_UK.csv').set_index('pcds')
        # with open('NW-postcodes.csv', 'w') as f:
        #     for row in postcode_locations.iterrows():
        #         if 'NW' in row[0]:
        #             f.write("new google.maps.LatLng({latitude}, {longitude}),\n".format(
        #                 latitude=row[1]['lat'],
        #                 longitude=row[1]['long']
        #             ))

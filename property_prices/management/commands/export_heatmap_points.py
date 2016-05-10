import numpy
import pandas

from django.core.management.base import BaseCommand

class Command(BaseCommand):

    help = "Export the coordinates and weights for the heatmap"

    def handle(self, *args, **options):

        # Geobounding box of England
        # top = 1.76896
        # bottom = -6.37988
        # left = 49.871159
        # right = 55.811741

        # Geobounding box of Greater London
        top = 0.3340155
        bottom = -0.5103751
        left = 51.2867602
        right = 51.6918741

        # Mesh resolution
        res = 100

        latitudes = numpy.linspace(left, right, res)
        longitudes = numpy.linspace(bottom, top, res)

        for latitude in latitudes:
            for longitude in longitudes:
                print "{location: new google.maps.LatLng(%s, %s), weight: %d}," % (latitude, longitude, numpy.random.random_integers(1, 100))


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

import pandas

from django.core.management.base import BaseCommand

class Command(BaseCommand):

    help = "Export the coordinates and weights for the heatmap"

    def handle(self, *args, **options):
        postcode_locations = pandas.read_csv('NSPL_FEB_2016_UK.csv').set_index('pcds')
        with open('workfile', 'w') as f:
            for row in postcode_locations.iterrows():
                f.write("new google.maps.LatLng({latitude}, {longitude}),\n".format(
                    latitude=row[1]['lat'],
                    longitude=row[1]['long']
                ))

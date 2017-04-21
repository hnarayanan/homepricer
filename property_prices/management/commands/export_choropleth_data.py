import pandas
import json

from django.core.management.base import BaseCommand
from django.db.models.aggregates import Count, Avg, Max, Min

from property_prices.models import Transaction


class Command(BaseCommand):

    help = "Export the average prices over time for rendering a choropleth"

    def add_arguments(self, parser):
        parser.add_argument('years', nargs='+', type=str)

    def handle(self, *args, **options):
        years = options['years']
        postcode_locations = pandas.read_csv('data/NSPL_FEB_2017_UK.csv').set_index('pcds')
        wards = postcode_locations.ward.unique()
        data = {}
        for year in years:
            for ward in wards:
#                aggregate = Transaction.objects.filter(property__ward=ward, transfer_date__year=year).aggregate(Count('price'), Avg('price'), Max('price'), Min('price'))
                average_price = Transaction.objects.filter(property__ward=ward, transfer_date__year=year).aggregate(Avg('price'))['price__avg']
                data[ward] = average_price
        print json.dumps(data)

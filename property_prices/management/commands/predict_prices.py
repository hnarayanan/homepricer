import datetime
import pandas

from django.core.management.base import BaseCommand, CommandError

from property_prices.models import Property, Transaction


class Command(BaseCommand):

    help = ""

    def handle(self, *args, **options):
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
        # TODO: Filter by 'transaction_category'? to only account for standard payments
        data = pandas.DataFrame()
        parse_date = lambda x: (datetime.datetime.strptime(x.replace(' 00:00', ''), '%Y-%m-%d').date() - datetime.date(1995, 01, 01)).days
        data['transfer_date'] = property_transactions['transaction_transfer_date'].map(parse_date)
        def get_latitude(postcode):
            try:
                return postcode_locations['lat'][postcode]
            except:
                return None
        def get_longitude(postcode):
            try:
                return postcode_locations['long'][postcode]
            except:
                return None
        data['latitude'] = property_transactions['property_postcode'].map(get_latitude)
        data['longitude'] = property_transactions['property_postcode'].map(get_longitude)
        data = pandas.concat([data, pandas.get_dummies(property_transactions['property_type'])], axis=1)
        data = pandas.concat([data, pandas.get_dummies(property_transactions['property_age'])], axis=1)
        data = pandas.concat([data, pandas.get_dummies(property_transactions['property_duration'])], axis=1)
        data['price'] = property_transactions['transaction_price']

        data.to_csv('data.csv')

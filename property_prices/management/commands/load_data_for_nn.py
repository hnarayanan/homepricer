import math
import datetime
import pandas

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    help = """
    This command loads property transaction data, combines it with
    post code geocode data and transforms the data to a format
    suitable for learning with neural networks. In particular,
    categorical inputs are "one-hot" encoded, continuous inputs are
    scaled to the range 0.0--1.0 and latitude and longitudes are
    converted to cartesian coordinates to make them more appropriate
    for calculating distances.
    """

    def handle(self, *args, **options):
        postcode_locations = pandas.read_csv('NSPL_MAY_2016_UK.csv').set_index('pcds')
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

        print data.describe()

        def rescale(data, column):
            return (data[column] - data[column].min())/(data[column].max() - data[column].min())

        data['transfer_date'] = rescale(data, 'transfer_date')
        data['price'] = rescale(data, 'price')

        # Leap of faith: http://mathworld.wolfram.com/SphericalCoordinates.html

        def geo_to_x(row):
            latitude = math.radians(row['latitude'])
            longitude = math.radians(row['longitude'])
            r = 1.0 # 6.371e6, but going to be rescaled anyway?
            return r*math.cos(latitude)*math.cos(longitude)

        def geo_to_y(row):
            latitude = math.radians(row['latitude'])
            longitude = math.radians(row['longitude'])
            r = 1.0 # 6.371e6, but going to be rescaled anyway?
            return r*math.cos(latitude)*math.sin(longitude)

        def geo_to_z(row):
            latitude = math.radians(row['latitude'])
            longitude = math.radians(row['longitude'])
            r = 1.0 # 6.371e6, but going to be rescaled anyway?
            return r*math.sin(latitude)

        data['x'] = data.apply(geo_to_x, axis=1)
        data['y'] = data.apply(geo_to_y, axis=1)
        data['z'] = data.apply(geo_to_z, axis=1)

        data['x'] = rescale(data, 'x')
        data['y'] = rescale(data, 'y')
        data['z'] = rescale(data, 'z')

        data.drop('latitude', axis=1, inplace=True)
        data.drop('longitude', axis=1, inplace=True)

        data.to_csv('data_normalized.csv')

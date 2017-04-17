import requests
import pandas
from StringIO import StringIO

from django.test import TestCase

from .models import Property


class DataImportTests(TestCase):

    def test_properties_match_postcode(self):

        property_transactions_csv = requests.get('http://landregistry.data.gov.uk/app/ppd/ppd_data.csv?et%5B%5D=lrcommon%3Afreehold&et%5B%5D=lrcommon%3Aleasehold&header=true&limit=all&nb%5B%5D=true&nb%5B%5D=false&postcode=nw3+6bg&ptype%5B%5D=lrcommon%3Adetached&ptype%5B%5D=lrcommon%3Asemi-detached&ptype%5B%5D=lrcommon%3Aterraced&ptype%5B%5D=lrcommon%3Aflat-maisonette&ptype%5B%5D=lrcommon%3AotherPropertyType&tc%5B%5D=ppd%3AstandardPricePaidTransaction&tc%5B%5D=ppd%3AadditionalPricePaidTransaction').content
        property_transactions = pandas.read_csv(StringIO(property_transactions_csv))

        for property in Property.objects.filter(postcode='NW3 6BG'):
            for transaction in properties.objects.all():
                print transaction


        # property_transactions_grouped = property_transactions.groupby([
        #                            'saon',
        #                            'paon',
        #                            'street',
        #                            'town',
        #                            'postcode',
        #                            'district',
        #                            'county'])

        # for property, transactions in property_transactions_grouped:
        #     print property

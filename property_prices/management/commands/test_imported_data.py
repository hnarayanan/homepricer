import pandas
import requests
from StringIO import StringIO

from django.core.management.base import BaseCommand, CommandError

from property_prices.models import Property


class Command(BaseCommand):

    help = "Test imported property and transaction data"

    def handle(self, *args, **options):

        print Property.objects.filter(postcode='SE19 1TQ').count()

        for property in Property.objects.filter(postcode='SE19 1TQ'):
            print property
            print property.transactions.count()
            for transaction in property.transactions.all():
                print transaction

            print '-'*72



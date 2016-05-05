from __future__ import unicode_literals

from django.db import models


class Property(models.Model):

    TYPES = (
        ('D', 'Detached'),
        ('S','Semi-Detached'),
        ('T', 'Terraced'),
        ('F', 'Flats/Maisonettes'),
        ('O', 'Other'),
    )

    AGES = (
        ('Y', 'Newly built'),
        ('N', 'Established building'),
    )

    DURATIONS = (
        ('F', 'Freehold'),
        ('L', 'Leasehold'),
    )

    paon = models.CharField(max_length=100, null=True)
    saon = models.CharField(max_length=100, null=True)
    street = models.CharField(max_length=100, null=True)
    locality = models.CharField(max_length=50, null=True)
    postcode = models.CharField(max_length=10, null=True)
    town_or_city = models.CharField(max_length=50, null=True)
    district = models.CharField(max_length=50, null=True)
    county = models.CharField(max_length=50, null=True)

    type = models.CharField(max_length=1, choices=TYPES)
    age = models.CharField(max_length=1, choices=AGES)
    duration = models.CharField(max_length=1, choices=DURATIONS)

    class Meta:
        verbose_name_plural = 'properties'

    def __unicode__(self):
        return '{saon}\n{paon} {street}\n{town_or_city}\n{postcode}'.format(
            paon=self.paon,
            saon=self.saon,
            street=self.street,
            town_or_city=self.town_or_city,
            postcode = self.postcode)

    def latest_price(self):
        return self.transactions.latest('transfer_date').price

    def latest_sale_date(self):
        return self.transactions.latest('transfer_date').transfer_date


class Transaction(models.Model):

    CATEGORIES = (
        ('A', 'Standard Price Paid'),
        ('B', ' Additional Price Paid'),
    )

    id = models.UUIDField(primary_key=True)
    property = models.ForeignKey(Property, related_name='transactions', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=0, null=True)
    category = models.CharField(max_length=1, choices=CATEGORIES)
    transfer_date = models.DateField(null=True)

    # TODO: Add a string representation of the model

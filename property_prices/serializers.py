from rest_framework import serializers

from .models import Property, Transaction


class PropertySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Property


class TransactionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Transaction

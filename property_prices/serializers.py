from rest_framework import serializers

from .models import Property, Transaction


class PropertySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Property
        fields = '__all__'


class TransactionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'

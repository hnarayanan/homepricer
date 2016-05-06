from rest_framework import viewsets

from .serializers import PropertySerializer, TransactionSerializer
from .models import Property, Transaction


class PropertyViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class TransactionViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

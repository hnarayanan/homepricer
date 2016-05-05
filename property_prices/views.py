from rest_framework import viewsets

from .serializers import PropertySerializer, TransactionSerializer
from .models import Property, Transaction


class PropertyViewSet(viewsets.ModelViewSet):

    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class TransactionViewSet(viewsets.ModelViewSet):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

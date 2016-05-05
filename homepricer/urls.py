from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from property_prices.views import PropertyViewSet, TransactionViewSet


router = routers.DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]

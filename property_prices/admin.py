from django.contrib import admin

from .models import Property, Transaction


admin.site.register(Property)
admin.site.register(Transaction)

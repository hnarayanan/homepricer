from django.contrib import admin

from .models import Property, Transaction


class PropertyAdmin(admin.ModelAdmin):

    list_display = ('__unicode__', 'type', 'age', 'duration',)
    list_filter = ('type', 'age', 'duration',)
    search_fields = ['paon', 'saon', 'street', 'locality', 'postcode',
                    'town_or_city', 'district', 'county']


class TransactionAdmin(admin.ModelAdmin):

    list_display = ('id', 'property', 'price', 'category',
                    'transfer_date',)
    list_filter = ('category', 'transfer_date',)
    search_fields = ['id']

    # TODO: Fields that aren't either searchable or filter-able
    # property = models.ForeignKey(Property, related_name='transactions', null=True)
    # price = models.DecimalField(max_digits=9, decimal_places=0, null=True)


admin.site.register(Property, PropertyAdmin)
admin.site.register(Transaction, TransactionAdmin)

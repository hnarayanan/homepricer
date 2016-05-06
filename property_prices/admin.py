from django.contrib import admin

from .models import Property, Transaction

class TransactionInline(admin.TabularInline):

    model = Transaction
    ordering = ('-transfer_date',)
    extra = 0


class PropertyAdmin(admin.ModelAdmin):

    list_display = ('__unicode__', 'latitude', 'longitude',
                    'latest_price', 'latest_transfer_date',
                    'type', 'age', 'duration')
    list_filter = ('type', 'age', 'duration',)
    search_fields = ['paon', 'saon', 'street', 'locality', 'postcode',
                    'town_or_city', 'district', 'county']
    fieldsets = (
        ('Property address', {
            'fields': ('saon', 'paon', 'street', 'locality',
                       'postcode', 'town_or_city', 'district',
                       'county', 'latitude', 'longitude',)
        }),
        ('About the property', {
            'fields': ('type', 'age', 'duration'),
        }),
    )
    inlines = [
        TransactionInline
    ]


class TransactionAdmin(admin.ModelAdmin):

    list_display = ('id', 'property', 'price', 'category',
                    'transfer_date',)
    list_filter = ('category', 'transfer_date',)
    search_fields = ['id']
    readonly_fields = ['property']

    # TODO: Fields that aren't either searchable or filter-able
    # property = models.ForeignKey(Property, related_name='transactions', null=True)
    # price = models.DecimalField(max_digits=9, decimal_places=0, null=True)

    fieldsets = (
        (None, {
            'fields': ('id', 'property', 'price', 'category', 'transfer_date')
        }),
    )

admin.site.register(Property, PropertyAdmin)
admin.site.register(Transaction, TransactionAdmin)

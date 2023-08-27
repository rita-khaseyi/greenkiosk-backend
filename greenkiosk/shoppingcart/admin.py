from django.contrib import admin
from .models import ShoppingCart

class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('get_product_name', 'get_quantity', 'get_price', 'get_total_price', 'date_created')

    def get_product_name(self, obj):
        return obj.product.name
    get_product_name.short_description = 'Product Name'

    def get_quantity(self, obj):
        return obj.quantity
    get_quantity.short_description = 'Quantity'

    def get_price(self, obj):
        return obj.product.price
    get_price.short_description = 'Price'

    def get_total_price(self, obj):
        return obj.total_price()
    get_total_price.short_description = 'Total Price'

admin.site.register(ShoppingCart, ShoppingCartAdmin)

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ShoppingCart

class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'quantity', 'price', 'total_price', 'date_created')

admin.site.register(ShoppingCart, ShoppingCartAdmin)


from django.contrib import admin
from .models import ShippingAddress, ShippingMethod

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address_line1', 'city', 'state', 'postal_code']

@admin.register(ShippingMethod)
class ShippingMethodAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost', 'delivery_time']


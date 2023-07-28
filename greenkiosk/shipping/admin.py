

from django.contrib import admin
from .models import Shipping

class ShippingAdmin(admin.ModelAdmin):
    list_display = ('order', 'carrier', 'tracking_number', 'status', 'estimated_delivery')

admin.site.register(Shipping, ShippingAdmin)

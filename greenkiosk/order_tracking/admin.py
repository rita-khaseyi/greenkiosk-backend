from django.contrib import admin
from .models import OrderTracking

class OrderTrackingAdmin(admin.ModelAdmin):
    list_display = ('id', 'tracking_number', 'shipping_carrier', 'tracking_status')

admin.site.register(OrderTracking, OrderTrackingAdmin)

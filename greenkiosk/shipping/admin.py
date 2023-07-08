# from django.contrib import admin
# from .models import Shipping

# # class ShippingAdmin(admin.ModelAdmin):
# #     list_display = ('order_number', 'carrier', 'tracking_number', 'status', 'estimated_delivery')

# # admin.site.register(Shipping, ShippingAdmin)


# # Make sure the attribute name 'order_number' matches the field name in the Shipping model
# class ShippingAdmin(admin.ModelAdmin):
#     list_display = ['order_number', 'carrier', 'tracking_number', 'status', 'estimated_delivery']

# admin.site.register(Shipping, ShippingAdmin)

from django.contrib import admin
from .models import Shipping

class ShippingAdmin(admin.ModelAdmin):
    list_display = ('order', 'carrier', 'tracking_number', 'status', 'estimated_delivery')

admin.site.register(Shipping, ShippingAdmin)

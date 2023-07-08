from django.contrib import admin


# Register your models here.
from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'quantity', 'total_price', 'date_created')

admin.site.register(Order, OrderAdmin)
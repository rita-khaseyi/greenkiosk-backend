from django.contrib import admin
from .models import Refund

class RefundAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'amount', 'reason', 'processed', 'date_created')

admin.site.register(Refund, RefundAdmin)

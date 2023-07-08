from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'payment_method', 'status', 'timestamp')

admin.site.register(Payment, PaymentAdmin)

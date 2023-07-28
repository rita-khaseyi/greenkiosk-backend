

from django.db import models
from orders.models import Order

class Shipping(models.Model):
    # shipping has a one-to-one relationship with the order model i.e each shipping instance
    # belongs to exactly one order
    order = models.OneToOneField(Order, on_delete=models.CASCADE,default=1)
    carrier = models.CharField(max_length=255)
    tracking_number = models.CharField(max_length=255)
    status = models.CharField(max_length=32)
    estimated_delivery = models.DateField()

    def __str__(self):
        return f"Shipping for Order {self.order}"

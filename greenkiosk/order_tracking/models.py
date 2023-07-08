from django.db import models

class OrderTracking(models.Model):
    tracking_number = models.CharField(max_length=50)
    shipping_carrier = models.CharField(max_length=50)
    tracking_status = models.CharField(max_length=100)

    def __str__(self):
        return f"Order Tracking #{self.id}"

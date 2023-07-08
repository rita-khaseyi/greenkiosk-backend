from django.db import models

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=255)
    transaction_id = models.CharField(max_length=255)
    status = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment ID: {self.id}"

from django.db import models

class Refund(models.Model):
    product_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    reason = models.TextField()
    processed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Refund for {self.product_name}"



# Create your models here.
from django.db import models

class Discount(models.Model):
    code = models.CharField(max_length=32, unique=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.code


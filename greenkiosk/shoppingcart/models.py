from django.db import models
from inventory.models import Product


class ShoppingCart(models.Model):
    products = models.ManyToManyField(Product)
    product_name = models.CharField(max_length=32)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Shopping Cart {self.pk}"

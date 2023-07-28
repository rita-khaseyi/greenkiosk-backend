# product.py
from django.db import models
from vendor.models import Vendor

class Product(models.Model):
    # one to many relationship between products and vendor
    # i.e one vendor can have multiple products
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product_images/',null=True)  # Added image field
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    id=models.PositiveIntegerField(primary_key=True)

    def __str__(self):
        return self.name

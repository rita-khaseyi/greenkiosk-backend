# reviews/models.py

from django.db import models
from django.contrib.auth.models import User
from inventory.models import Product

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    rating = models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"

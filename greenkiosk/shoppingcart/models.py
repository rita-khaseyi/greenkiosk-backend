from django.contrib.auth.models import User
from django.db import models
from inventory.models import Product

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    products = models.ManyToManyField(Product, through='CartItem')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def total_price(self):
        return sum(cart_item.total_price() for cart_item in self.cart_items.all())

    def __str__(self):
       return f"Shopping Cart {self.pk}"

class CartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

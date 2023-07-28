

from django.db import models
from payment.models import Payment
from inventory.models import Product
from customer.models import Customer
from shoppingcart.models import ShoppingCart

class Order(models.Model):
    # onetoone relationship between order and payment i.e each order instance is associated with 
    # one payment instance.
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, null=True)
    # one to many relationship between order and product i.e  each Order instance can be associated with
    # one Product instance, but a Product instance can be related to multiple Order instances.
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    product_name = models.CharField(max_length=32)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    #  order has one-to-many relationship with the Customer model using the ForeignKey field 
    # type. i.e each Order instance is associated with one Customer instance, but a Customer 
    # instance can have multiple related Order instances.
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    # order has many-to-many relationship with the ShoppingCart model 
    # i.e multiple Order instances can be associated with multiple ShoppingCart instances, and vice versa.
    shopping_carts = models.ManyToManyField(ShoppingCart)

    def __str__(self):
        return f"Order {self.pk}"

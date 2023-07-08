

# # from django.db import models
# # from payment.models import Payment
# # from inventory.models import Product

# # class Order(models.Model):
# #     payment = models.OneToOneField(Payment, on_delete=models.CASCADE, null=True)
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
# #     product_name = models.CharField(max_length=32)
# #     quantity = models.PositiveIntegerField()
# #     total_price = models.DecimalField(max_digits=8, decimal_places=2)
# #     date_created = models.DateTimeField(auto_now_add=True)
# #     date_updated = models.DateTimeField(auto_now=True)

# #     def __str__(self):
# #         return f"Order {self.pk}"


# from django.db import models
# from payment.models import Payment
# from inventory.models import Product
# from customer.models import Customer

# class Order(models.Model):
#     payment = models.OneToOneField(Payment, on_delete=models.CASCADE, null=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
#     product_name = models.CharField(max_length=32)
#     quantity = models.PositiveIntegerField()
#     total_price = models.DecimalField(max_digits=8, decimal_places=2)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return f"Order {self.pk}"


from django.db import models
from payment.models import Payment
from inventory.models import Product
from customer.models import Customer
from shoppingcart.models import ShoppingCart

class Order(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    product_name = models.CharField(max_length=32)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    shopping_carts = models.ManyToManyField(ShoppingCart)

    def __str__(self):
        return f"Order {self.pk}"

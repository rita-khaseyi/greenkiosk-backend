from rest_framework import serializers
from customer.models import Customer
from inventory.models import Product
from orders.models import Order
from shoppingcart.models import ShoppingCart

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"
# products class
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"     
        image = serializers.ImageField(max_length=None, use_url=True)        


# orders

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"     


# cart
class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'




class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(default=1)

    def validate(self, data):
        # Check if the product exists
        product_id = data['product_id']
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product does not exist")
        
        # Check if the quantity is positive
        if data['quantity'] <= 0:
            raise serializers.ValidationError("Quantity must be greater than zero")
        
        return data
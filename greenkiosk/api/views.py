from rest_framework.views import APIView
from customer.models import Customer
from inventory.models import Product
from orders.models import Order
from shoppingcart.models import ShoppingCart,CartItem
from .serializers import CustomerSerializer,ProductSerializer,OrderSerializer
from rest_framework.response import Response
from rest_framework import status
from .serializers import ShoppingCartSerializer
from rest_framework import viewsets
from rest_framework.decorators import action

class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CustomerDetailView(APIView):
    def get(self, request,id,format=None):
        customer=Customer.objects.get(id=id)
        serializer=CustomerSerializer(customer)
        return Response(serializer.data)
    def put(self,request,id,format=None):
        customer=Customer.objects.get(id=id)
        serializer=CustomerSerializer(customer,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id,format=None):
        customer=Customer.objects.get(id=id)
        customer.delete()
        return Response("customer deleted",status=status.HTTP_204_NO_CONTENT)  


# 1) As we have done with the Customer Model, create ListAPIView and DetailAPIView for each of these models.
# Product
# Basket
# Order
# 2) Each ListAPIView should have GET, POST
# 3) Each DetailAPIView should have GET, PUT, and DELETE HTTP Methods.
# 4) You should also add the appropriate URLs for each API
# 5) For the basket DetailAPIView, add a method that adds a product to the basket and returns an instance of the basket
#    
 # Products apis

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ProductDetailView(APIView):
    def get(self, request,id,format=None):
        product=Product.objects.get(id=id)
        serializer=ProductSerializer(product)
        return Response(serializer.data)
    def put(self,request,id,format=None):
        customer=Product.objects.get(id=id)
        serializer=ProductSerializer(Product,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id,format=None):
        customer=Product.objects.get(id=id)
        customer.delete()
        return Response("Product deleted",status=status.HTTP_204_NO_CONTENT)      
    

# Orders Apis

class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class OrderDetailView(APIView):
    def get(self, request,id,format=None):
        order=Order.objects.get(id=id)
        serializer=OrderSerializer(order)
        return Response(serializer.data)
    def put(self,request,id,format=None):
        order=Order.objects.get(id=id)
        serializer=OrderSerializer(order,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id,format=None):
        customer=Order.objects.get(id=id)
        customer.delete()
        return Response("order deleted",status=status.HTTP_204_NO_CONTENT)      

# cart   



class CartListView(APIView):
    def get(self, request):
        carts = ShoppingCart.objects.all()
        serializer = ShoppingCartSerializer(carts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShoppingCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CartDetailView(APIView):
    def get(self, request, pk):
        cart = ShoppingCart.objects.get(pk=pk)
        serializer = ShoppingCartSerializer(cart)
        return Response(serializer.data)

    def put(self, request, pk):
        cart = ShoppingCart.objects.get(pk=pk)
        serializer = ShoppingCartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cart = ShoppingCart.objects.get(pk=pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import AddToCartSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    serializer = AddToCartSerializer(data=request.data)
    if serializer.is_valid():
        product_id = serializer.validated_data['product_id']
        quantity = serializer.validated_data['quantity']
        
        # Get or create the user's shopping cart
        user = request.user  # Get the authenticated user
        user_cart, created = ShoppingCart.objects.get_or_create(user=user)
        
        # Add the product to the cart or update the quantity if it already exists
        cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product_id=product_id)
        cart_item.quantity += quantity
        cart_item.save()
        
        return Response({"message": "Product added to cart successfully", "cart_id": user_cart.pk}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
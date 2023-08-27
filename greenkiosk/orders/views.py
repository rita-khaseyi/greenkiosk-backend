# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem
from .forms import OrderForm
from shoppingcart.models import ShoppingCart

def create_order(request):
    cart = ShoppingCart.objects.get(user=request.user)
    total_price = cart.total_price
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = total_price
            order.save()
            
            for cart_item in cart.cart_items.all():
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    unit_price=cart_item.product.price,
                    total_price=cart_item.total_price
                )
            
            # Clear the cart
            cart.cart_items.all().delete()
            
            return redirect('order_confirmation', order_id=order.id)
    else:
        form = OrderForm()
        
    context = {
        'form': form,
        'total_price': total_price,
    }
    return render(request, 'orders/create_order.html', context)

def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {
        'order': order,
    }
    return render(request, 'orders/order_confirmation.html', context)

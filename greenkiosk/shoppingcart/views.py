# shoppingcart/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ShoppingCart, CartItem,Product

from django.shortcuts import get_object_or_404

@login_required
def view_cart(request):
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)
    selected_product_id = request.GET.get('selected_product_id')
    cart_items = cart.cart_items.all()
    total_price = cart.total_price()

    selected_product = None
    selected_cart_item = None
    if selected_product_id:
        selected_product = get_object_or_404(Product, id=selected_product_id)
        selected_cart_item = cart_items.filter(product=selected_product).first()

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price,
        'selected_product': selected_product,
        'selected_cart_item': selected_cart_item,
    }
    return render(request, 'cart/view_cart.html', context)


from django.shortcuts import get_object_or_404

@login_required
def add_to_cart(request, product_id):
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)  # Retrieve the specific product using get_object_or_404
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    if cart_item.cart.user == request.user:
        cart_item.delete()
    return redirect('view_cart')
from django.http import HttpResponseRedirect

@login_required
def update_cart_quantity(request, cart_item_id):
    if request.method == "POST":
        action = request.POST.get("action")
        cart_item = CartItem.objects.get(id=cart_item_id)
        
        if action == "increase":
            cart_item.quantity += 1
        elif action == "decrease" and cart_item.quantity > 1:
            cart_item.quantity -= 1
        
        cart_item.save()
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

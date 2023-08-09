from django.shortcuts import render,redirect
from .forms import ShoppingUploadForm
from .models import ShoppingCart


# Create your views here.
def upload_Cart(request):
    if request.method == 'POST':
        form = ShoppingUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    else:
      form = ShoppingUploadForm()
     
    return render(request,'cart/shoppingcart_upload.html',{'form':form})

def shopping_list(request):
    shopping=ShoppingCart.objects.all()
    return render(request,'cart/cart_list.html',{'shoppings':shopping})

def  shopping_detail(request,id):
    cart=ShoppingCart.objects.get(id=id)
    return render(request,'cart/cart_detail.html',{'cart':cart})

def edit_shopping_view(request,id):
    cart=ShoppingCart.objects.get(id=id)
    if request.method == 'POST':
        form=ShoppingUploadForm(request.POST,instance=cart)
        if form.is_valid():
            form.save()
        return redirect('cart_detail_view,id=id')     
    else:
        form=ShoppingUploadForm(request.POST,instance=cart)
        return render(request,'cart/edit_cart.html',{'form':form  })     


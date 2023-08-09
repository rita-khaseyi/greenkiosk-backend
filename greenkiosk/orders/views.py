from django.shortcuts import render,redirect
from .forms import ordersUploadForm
from .models import Order


# Create your views here.
def upload_order(request):
    if request.method == 'POST':
        form = ordersUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    else:
      form = ordersUploadForm()
     
    return render(request,'orders/orders_upload.html',{'form':form})
def order_list(request):
    order=Order.objects.all()
    return render(request,'orders/orders_list.html',{'orders':order})
def  order_detail(request,id):
    cart=Order.objects.get(id=id)
    return render(request,'orders/orders_detail.html',{'order':cart})

def edit_order_view(request,id):
    order=Order.objects.get(id=id)
    if request.method == 'POST':
        form=ordersUploadForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
        return redirect('orders_detail_view,id=id')     
    else:
        form=ordersUploadForm(request.POST,instance=order)
        return render(request,'orders/edit_orders.html',{'form':form  })     


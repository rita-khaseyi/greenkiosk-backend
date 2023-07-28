from django.shortcuts import render
from .forms import ProductUploadForm
from .models import Product

# Create your views here.

def upload_product(request):
    if request.method == 'POST':
        form = ProductUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    else:
      form = ProductUploadForm()
     
    return render(request,'inventory/product_upload.html',{'form':form})
   
    # render accepts a request and the template where its going to render the request and the data to render
    # and the third is the data to be uploaded
def product_list(request):
    products=Product.objects.all()
    return render(request,'inventory/products_list.html',{'products':products})
def  product_detail(request,id):
    product=Product.objects.get(id=id)
    return render(request,'inventory/product_detail.html',{'product':product})



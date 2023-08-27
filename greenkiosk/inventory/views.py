from django.shortcuts import render,redirect
from .forms import ProductUploadForm
from .models import Product 
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Product
from reviews.forms import ReviewForm  # Import the ReviewForm
from reviews.models import Review

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


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()

    context = {
        'product': product,
        'form': form,
    }

    return render(request, 'inventory/product_detail.html', context)

def edit_product_view(request,id):
    produduct=Product.objects.get(id=id)
    if request.method == 'POST':
        form=ProductUploadForm(request.POST,instance=produduct)
        if form.is_valid():
            form.save()
        return redirect('products_detail_view,id=id')     
    else:
        form=ProductUploadForm(request.POST,instance=produduct)
        return render(request,'inventory/edit_product.html',{'form':form  })     

def product_search(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        products = Product.objects.all()
    return render(request, 'inventory/product_search.html', {'products': products})
def product_reviews(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)
    
    context = {
        'product': product,
        'reviews': reviews,
    }
    
    return render(request, 'inventory/product_reviews.html', context)



# Create your views here.
from django.shortcuts import render,redirect
from .forms import DiscountUploadForm
from .models import Discount



def upload_discount(request):
    if request.method == 'POST':
        form = DiscountUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    else:
      form = DiscountUploadForm()
     
    return render(request,'discount/discount_upload.html',{'form':form})
   
    # render accepts a request and the template where its going to render the request and the data to render
    # and the third is the data to be uploaded
def discount_list(request):
    discounts=Discount.objects.all()
    return render(request,'discount/discount_list.html',{'discounts':discounts})
def  discount_detail(request,id):
    discounts=Discount.objects.get(id=id)
    return render(request,'discount/discount_detail.html',{'discount':discounts})

def edit_discount_view(request,id):
    discount=Discount.objects.get(id=id)
    if request.method == 'POST':
        form=DiscountUploadForm(request.POST,instance=discount)
        if form.is_valid():
            form.save()
        return redirect('discount_detail_view,id=id')     
    else:
        form=DiscountUploadForm(request.POST,instance=discount)
        return render(request,'discount/edit_discount.html',{'form':form  })     







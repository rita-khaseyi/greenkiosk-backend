from django.shortcuts import render,redirect
from .forms import PaymentUploadForm
from .models import Payment
# Create your views here.

def upload_product(request):
    if request.method == 'POST':
        form = PaymentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    else:
      form = PaymentUploadForm()
     
    return render(request,'payment/paymentupload.html',{'form':form})
def payment_list(request):
    payments=Payment.objects.all()
    return render(request,'payment/payment_list.html',{'payments':payments})
def  payment_detail(request,id):
    payment=Payment.objects.get(id=id)
    return render(request,'payment/payment_detail.html',{'payment':payment})

def edit_payment_view(request,id):
    payment=Payment.objects.get(id=id)
    if request.method == 'POST':
        form=PaymentUploadForm(request.POST,instance=payment)
        if form.is_valid():
            form.save()
        return redirect('payment_detail_view,id=id')     
    else:
        form=PaymentUploadForm(request.POST,instance=payment)
        return render(request,'payment/edit_payment.html',{'form':form  })    
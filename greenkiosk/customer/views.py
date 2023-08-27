from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('products_list_view')  
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('products_list_view') 

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after successful registration
            login(request, user)
            return redirect('products_list_view')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# from django.shortcuts import render,redirect
# from .forms import CustomerUploadForm
# from .models import Customer

# # Create your views here.


# def upload_customer(request):
#     if request.method == 'POST':
#         form = CustomerUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
            
#     else:
#       form = CustomerUploadForm()
     
#     return render(request,'customer/customer_upload.html',{'form':form})
   
# def customer_list(request):
#     customers=Customer.objects.all()
#     return render(request,'customer/customer_list.html',{'customers':customers})
# def  customer_detail(request,id):
#     customer=Customer.objects.get(id=id)
#     return render(request,'customer/customer_detail.html',{'customer':customer})
# def edit_customer_view(request,id):
#     customer=Customer.objects.get(id=id)
#     if request.method == 'POST':
#         form=CustomerUploadForm(request.POST,instance=customer)
#         if form.is_valid():
#             form.save()
#         return redirect('customer_detail_view,id=id')     
#     else:
#         form=CustomerUploadForm(request.POST,instance=customer)
#         return render(request,'customer/edit_customer.html',{'form':form  })     

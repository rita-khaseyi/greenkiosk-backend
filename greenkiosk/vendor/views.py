from django.shortcuts import render, redirect
from .forms import VendorUploadForm
from .models import Vendor

# Create your views here.
def upload_vendor(request):
    if request.method == 'POST':
        form = VendorUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vendor_list_view')  # Redirect to the review list view
    else:
        form = VendorUploadForm()
    return render(request, 'vendor/vendor_upload.html', {'form': form})

def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor/vendor_list.html', {'vendors': vendors})

def vendor_detail(request, id):
    vendor = Vendor.objects.get(id=id)
    return render(request, 'vendor/vendor_detail.html', {'vendor': vendor})

def vendor_edit_view(request, id):
    vendor = Vendor.objects.get(id=id)
    if request.method == 'POST':
        form = VendorUploadForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('vendor_detail_view', id=id)  # Redirect to the review detail view
    else:
        form = VendorUploadForm(instance=vendor)
    return render(request, 'vendor/edit_vendor.html', {'form': form})

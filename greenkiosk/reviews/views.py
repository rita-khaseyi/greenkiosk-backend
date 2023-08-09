from django.shortcuts import render, redirect
from .forms import reviewUploadForm
from .models import Review

# Create your views here.
def upload_review(request):
    if request.method == 'POST':
        form = reviewUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('review_list_view')  # Redirect to the review list view
    else:
        form = reviewUploadForm()
    return render(request, 'review/review_upload.html', {'form': form})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review/review_list.html', {'reviews': reviews})

def review_detail(request, id):
    review = Review.objects.get(id=id)
    return render(request, 'review/review_detail.html', {'review': review})

def review_edit_view(request, id):
    review = Review.objects.get(id=id)
    if request.method == 'POST':
        form = reviewUploadForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_detail_view', id=id)  # Redirect to the review detail view
    else:
        form = reviewUploadForm(instance=review)
    return render(request, 'review/edit_review.html', {'form': form})

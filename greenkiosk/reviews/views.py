from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from inventory.models import Product
from reviews.models import Review
from django.http import JsonResponse

@login_required
def submit_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()

            # Redirect to the product detail view
            return redirect('products_detail_view', id=product.id)  # Adjust the URL name

    else:
        form = ReviewForm()

    reviews = Review.objects.filter(product=product)  # Get reviews for the product
    context = {
        'product': product,
        'form': form,
        'reviews': reviews,
    }

    return render(request, 'review/submit_review.html', context)

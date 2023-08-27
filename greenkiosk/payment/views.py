from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Payment
from shoppingcart.models import ShoppingCart

@login_required
def make_payment(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        payment_method = request.POST['payment_method']
        transaction_id = 134567

        payment = Payment.objects.create(
            user=request.user,
            amount=amount,
            payment_method=payment_method,
            transaction_id=transaction_id,
            status='pending'
        )

        return redirect('payment:payment_confirmation', payment_id=payment.id)

    # Get the total price from the cart
    cart = ShoppingCart.objects.get_or_create(user=request.user)[0]
    total_price = cart.total_price()

    return render(request, 'payment/make_payment.html', {'total_price': total_price})

@login_required
def user_payments(request):
    payments = Payment.objects.filter(user=request.user)
    return render(request, 'payment/user_payments.html', {'payments': payments})
@login_required
def payment_confirmation(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id, user=request.user)
    return render(request, 'payment/payment_confirmation.html', {'payment': payment})

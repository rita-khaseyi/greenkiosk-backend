

# forms.py
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    shipping_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter shipping address'}))
    payment_method = forms.ChoiceField(choices=[
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
    ], widget=forms.RadioSelect)
    
    class Meta:
        model = Order
        fields = ['shipping_address', 'payment_method']

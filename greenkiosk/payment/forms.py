from django import forms
from .models import Payment

class PaymentUploadForm(forms.ModelForm): 
    
    class Meta:
        # defines the model
        model = Payment
        # renders all the fields in the form
        fields = "__all__"

        



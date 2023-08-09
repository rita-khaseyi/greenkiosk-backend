from django import forms
from .models import Shipping

class ShippingUploadForm(forms.ModelForm): 
    
    class Meta:
        # defines the model
        model = Shipping
        # renders all the fields in the form
        fields = "__all__"

        



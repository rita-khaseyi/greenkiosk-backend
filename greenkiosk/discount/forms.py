from django import forms
from .models import Discount

class DiscountUploadForm(forms.ModelForm): 
    
    class Meta:
        # defines the model
        model = Discount
        # renders all the fields in the form
        fields = "__all__"

        



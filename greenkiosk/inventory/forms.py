from django import forms
from .models import Product

class ProductUploadForm(forms.ModelForm): 
    
    class Meta:
        # defines the model
        model = Product
        # renders all the fields in the form
        fields = "__all__"

        



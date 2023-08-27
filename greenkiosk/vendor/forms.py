from django import forms
from .models import Vendor

class VendorUploadForm(forms.ModelForm): 
    
    class Meta:
        # defines the model
        model = Vendor
        # renders all the fields in the form
        fields = "__all__"

        



from django import forms
from .models import Customer

class CustomerUploadForm(forms.ModelForm): 
    
    class Meta:
        # defines the model
        model = Customer
        # renders all the fields in the form
        fields = "__all__"

        



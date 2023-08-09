from django import forms
from .models import Review

class reviewUploadForm(forms.ModelForm): 
    
    class Meta:
        # defines the model
        model = Review
        # renders all the fields in the form
        fields = "__all__"

        



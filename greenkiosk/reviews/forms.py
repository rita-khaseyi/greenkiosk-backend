from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content']
        widgets = {
            'rating': forms.RadioSelect(attrs={'class': 'rating-radio'}),
            'content': forms.Textarea(attrs={'class': 'review-content'}),
        }

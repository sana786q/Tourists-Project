from django import forms
from .models import ShoppingMallReviewRating

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ShoppingMallReviewRating
        fields = ['subject', 'review', 'rating'] 
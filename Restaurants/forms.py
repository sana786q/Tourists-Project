from django import forms
from .models import RestaurantReviewRating

class ReviewForm(forms.ModelForm):
    class Meta:
        model = RestaurantReviewRating
        fields = ['subject', 'review', 'rating'] 
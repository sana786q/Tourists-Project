from django import forms
from .models import TourismPlaceReviewRating

class ReviewForm(forms.ModelForm):
    class Meta:
        model = TourismPlaceReviewRating
        fields = ['subject', 'review', 'rating'] 
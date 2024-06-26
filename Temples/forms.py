from django import forms
from .models import TempleReviewRating

class ReviewForm(forms.ModelForm):
    class Meta:
        model = TempleReviewRating
        fields = ['subject', 'review', 'rating'] 
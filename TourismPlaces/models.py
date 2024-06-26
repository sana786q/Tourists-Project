from django.db import models
from accounts.models import Account

# Create your models here.

class TourismPlaces(models.Model):
    place_name = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=250, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    place_pictures1 = models.ImageField(upload_to='TourismPlaces', blank=False)
    place_pictures2 = models.ImageField(upload_to='TourismPlaces', blank=True)
    place_pictures3 = models.ImageField(upload_to='TourismPlaces', blank=True)
    place_pictures4 = models.ImageField(upload_to='TourismPlaces', blank=True)
    place_pictures5 = models.ImageField(upload_to='TourismPlaces', blank=True)
    place_pictures6 = models.ImageField(upload_to='TourismPlaces', blank=True)
    place_pictures7 = models.ImageField(upload_to='TourismPlaces', blank=True)
    place_pictures8 = models.ImageField(upload_to='TourismPlaces', blank=True)
    
    
    class Meta:
        verbose_name = 'Tourism Places'
        verbose_name_plural = 'Tourism Places'
    
    def __str__(self):
        return self.place_name

    def __str__(self):
        return self.location
    
    
class TourismPlaceReviewRating(models.Model):
    # hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject
    
    
class VisitLaterTP(models.Model):
    place_name = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=250, blank=False)
    category = models.CharField(max_length=50, blank=False, default="Tourism_Places")
    
    class Meta:
        verbose_name = 'VisitLaterTP'
        verbose_name_plural = 'Visit Later'

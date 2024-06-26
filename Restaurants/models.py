from django.db import models
from accounts.models import Account

# Create your models here.

class Restaurants(models.Model):
    restaurant_name = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=250, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    opening_time = models.CharField(max_length=10, blank=True)
    closing_time = models.CharField(max_length=10, blank=True)
    contact = models.CharField(max_length=12, blank=True)
    restaurant_pictures1 = models.ImageField(upload_to='Restaurants', blank=False)
    restaurant_pictures2 = models.ImageField(upload_to='Restaurants', blank=True)
    restaurant_pictures3 = models.ImageField(upload_to='Restaurants', blank=True)
    restaurant_pictures4 = models.ImageField(upload_to='Restaurants', blank=True)
    restaurant_pictures5 = models.ImageField(upload_to='Restaurants', blank=True)
    restaurant_pictures6 = models.ImageField(upload_to='Restaurants', blank=True)
    restaurant_pictures7 = models.ImageField(upload_to='Restaurants', blank=True)
    restaurant_pictures8 = models.ImageField(upload_to='Restaurants', blank=True)

    
    class Meta:
        verbose_name = 'Restaurants'
        verbose_name_plural = 'Restaurants'
    
    def __str__(self):
        return self.restaurant_name

    def __str__(self):
        return self.location
    
    
class RestaurantReviewRating(models.Model):
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
    
    
class VisitLaterR(models.Model):
    restaurant_name = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=250, blank=False)
    category = models.CharField(max_length=50, blank=False, default="Restaurant")
    
    class Meta:
        verbose_name = 'VisitLaterR'
        verbose_name_plural = 'Visit Later'
    

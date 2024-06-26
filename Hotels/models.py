from django.db import models
from accounts.models import Account

# Create your models here.

class Hotels(models.Model):
    hotel_name = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=250, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    check_in_time = models.CharField(max_length=10, blank=True)
    check_out_time = models.CharField(max_length=10, blank=True)
    contact1 = models.CharField(max_length=12, blank=True)
    contact2 = models.CharField(max_length=12, blank=True)
    hotel_pictures1 = models.ImageField(upload_to='Hotels', blank=False)
    hotel_pictures2 = models.ImageField(upload_to='Hotels', blank=True)
    hotel_pictures3 = models.ImageField(upload_to='Hotels', blank=True)
    hotel_pictures4 = models.ImageField(upload_to='Hotels', blank=True)
    hotel_pictures5 = models.ImageField(upload_to='Hotels', blank=True)
    hotel_pictures6 = models.ImageField(upload_to='Hotels', blank=True)
    hotel_pictures7 = models.ImageField(upload_to='Hotels', blank=True)
    hotel_pictures8 = models.ImageField(upload_to='Hotels', blank=True)

    
    class Meta:
        verbose_name = 'Hotels'
        verbose_name_plural = 'Hotels'
    
    def __str__(self):
        return self.hotel_name

    def __str__(self):
        return self.location
    
    def access_name(self):
        return f'{self.hotel_name.split(" ")}'

    
    
class ReviewRating(models.Model):
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
    
    
class VisitLater(models.Model):
    hotel_name = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=250, blank=False)
    category = models.CharField(max_length=50, blank=False, default="Hotel")
    
    class Meta:
        verbose_name = 'VisitLater'
        verbose_name_plural = 'Visit Later'
    
    
    
    
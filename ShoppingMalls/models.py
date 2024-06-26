from django.db import models
from accounts.models import Account

# Create your models here.

class ShoppingMalls(models.Model):
    mall_name = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=250, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    opening_time = models.CharField(max_length=10, blank=True)
    closing_time = models.CharField(max_length=10, blank=True)
    contact = models.CharField(max_length=12, blank=True)
    mall_pictures1 = models.ImageField(upload_to='ShoppingMalls', blank=False)
    mall_pictures2 = models.ImageField(upload_to='ShoppingMalls', blank=True)
    mall_pictures3 = models.ImageField(upload_to='ShoppingMalls', blank=True)
    mall_pictures4 = models.ImageField(upload_to='ShoppingMalls', blank=True)
    
    class Meta:
        verbose_name = 'Shopping Malls'
        verbose_name_plural = 'Shopping Malls'
    
    def __str__(self):
        return self.mall_name

    def __str__(self):
        return self.location
    
    
class ShoppingMallReviewRating(models.Model):
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
    
    
class VisitLaterS(models.Model):
    mall_name = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=250, blank=False)
    category = models.CharField(max_length=50, blank=False, default="Shopping_Mall")
    
    class Meta:
        verbose_name = 'VisitLaterS'
        verbose_name_plural = 'Visit Later'



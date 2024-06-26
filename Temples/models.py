from django.db import models
from accounts.models import Account

# Create your models here.

class Temples(models.Model):
    temple_name = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=250, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    temple_pictures1 = models.ImageField(upload_to='Temples', blank=False)
    temple_pictures2 = models.ImageField(upload_to='Temples', blank=True)
    temple_pictures3 = models.ImageField(upload_to='Temples', blank=True)
    temple_pictures4 = models.ImageField(upload_to='Temples', blank=True)
    
    class Meta:
        verbose_name = 'Temples'
        verbose_name_plural = 'Temples'
    
    def __str__(self):
        return self.temple_name

    def __str__(self):
        return self.location
    
    
class TempleReviewRating(models.Model):
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


class VisitLaterT(models.Model):
    temple_name = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=250, blank=False)
    category = models.CharField(max_length=50, blank=False, default="Temple")
    
    class Meta:
        verbose_name = 'VisitLaterT'
        verbose_name_plural = 'Visit Later'

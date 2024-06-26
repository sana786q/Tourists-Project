from django.db import models

# Create your models here.

class Features(models.Model):
    category_name = models.CharField(max_length=50)
    category_picture_name = models.CharField(max_length=50)
    category_description = models.TextField(max_length=500)
    category_picture1 = models.ImageField(upload_to='features')
    category_picture2 = models.ImageField(upload_to='features', blank=True)
    
    class Meta:
        verbose_name = 'Features'
        verbose_name_plural = 'Features'
        
    def __str__(self):
        return self.category_picture_name
    

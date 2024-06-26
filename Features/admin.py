from django.contrib import admin
from .models import Features

# Register your models here.

class FeaturesAdmin(admin.ModelAdmin):
    
    list_display = ('category_name', 'category_picture_name')

admin.site.register(Features, FeaturesAdmin)

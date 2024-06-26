from django.contrib import admin
from .models import Hotels, ReviewRating, VisitLater

# Register your models here.

class HotelsAdmin(admin.ModelAdmin):
    
    list_display = ('hotel_name', 'location')
    
    
class VisitLaterAdmin(admin.ModelAdmin):
     
     list_display = ('hotel_name', 'location')

admin.site.register(Hotels, HotelsAdmin)
admin.site.register(ReviewRating)
admin.site.register(VisitLater, VisitLaterAdmin)




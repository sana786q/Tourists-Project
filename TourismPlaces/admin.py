from django.contrib import admin
from .models import TourismPlaces, TourismPlaceReviewRating, VisitLaterTP

# Register your models here.

class TourismPlacesAdmin(admin.ModelAdmin):
    
    list_display = ('place_name', 'location')
    
    
class VisitLaterTPAdmin(admin.ModelAdmin):
     
     list_display = ('place_name', 'location')

admin.site.register(TourismPlaces, TourismPlacesAdmin)
admin.site.register(TourismPlaceReviewRating)
admin.site.register(VisitLaterTP, VisitLaterTPAdmin)



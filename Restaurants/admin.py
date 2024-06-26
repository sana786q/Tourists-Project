from django.contrib import admin
from .models import Restaurants, RestaurantReviewRating, VisitLaterR

# Register your models here.

class RestaurantsAdmin(admin.ModelAdmin):
    
    list_display = ('restaurant_name', 'location')
    

class VisitLaterRAdmin(admin.ModelAdmin):
     
     list_display = ('restaurant_name', 'location')

admin.site.register(Restaurants, RestaurantsAdmin)
admin.site.register(RestaurantReviewRating)
admin.site.register(VisitLaterR, VisitLaterRAdmin)



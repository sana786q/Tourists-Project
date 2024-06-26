from django.contrib import admin
from .models import ShoppingMalls, ShoppingMallReviewRating, VisitLaterS

# Register your models here.

class ShoppingMallsAdmin(admin.ModelAdmin):
    
    list_display = ('mall_name', 'location')
    
    
class VisitLaterSAdmin(admin.ModelAdmin):
     
     list_display = ('mall_name', 'location')


admin.site.register(ShoppingMalls, ShoppingMallsAdmin)
admin.site.register(ShoppingMallReviewRating)
admin.site.register(VisitLaterS, VisitLaterSAdmin)


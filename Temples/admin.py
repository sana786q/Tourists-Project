from django.contrib import admin
from .models import Temples, TempleReviewRating, VisitLaterT

# Register your models here.

class TemplesAdmin(admin.ModelAdmin):
    
    list_display = ('temple_name', 'location')
    
    
class VisitLaterTAdmin(admin.ModelAdmin):
     
     list_display = ('temple_name', 'location')


admin.site.register(Temples, TemplesAdmin)
admin.site.register(TempleReviewRating)
admin.site.register(VisitLaterT, VisitLaterTAdmin)



from django.shortcuts import render
from .models import Features

# Create your views here.

def features(request):
    
    Feature = Features.objects.all()
    context = {
        'Feature' : Feature
    }
    return(request, context)

def aboutus(request):
    return render(request, "about.html")

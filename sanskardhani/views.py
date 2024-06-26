from django.shortcuts import render, redirect
from django.http import HttpResponse
from Features.models import Features

# Create your views here.

def sanskardhani(request):
    
    allobject = Features.objects.all()
    context = {
        'allobject' : allobject
    }
    
    return render(request, "home.html", context)
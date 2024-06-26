from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TourismPlaces, TourismPlaceReviewRating, VisitLaterTP
from django.contrib import  messages

# Create your views here.

def tourismplaces(request):
    
    allobject = TourismPlaces.objects.all()
    context = {
        'allobject' : allobject
    }
    return render(request, "tourismplaces.html", context)

def places(request, id):
    
    places = TourismPlaces.objects.get(id=id)
    reviews = TourismPlaceReviewRating.objects.filter(status=True)
    data = {
        'places' : places,
        'reviews' : reviews
    }
    return render(request, "single_tourism_place.html", data)


def submit_review(request, id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = TourismPlaceReviewRating()
            data.subject = form.cleaned_data['subject']
            data.rating = form.cleaned_data['rating']
            data.review = form.cleaned_data['review']
            data.ip = request.META.get('REMOTE_ADDR')
            data.id = id
            data.user_id = request.user.id
            data.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect('tourismplaces')               
        
    else:
        return HttpResponse("fail")
    
def AddMarkedPlacesTP(request, id):
    addplace = TourismPlaces.objects.get(id=id)
    if request.user.is_authenticated:
        data = VisitLaterTP()
        if VisitLaterTP.objects.filter(place_name=addplace.place_name).exists():
            pass
        else:
            data.place_name = addplace.place_name
            data.location = addplace.location
            data.save()
        
    return render(request, "accounts/profile.html")



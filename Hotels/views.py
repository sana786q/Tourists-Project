from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hotels, ReviewRating, VisitLater
from .forms import ReviewForm
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

# def _hotel_id(request):
#     hotelid = request.session.session_key
#     if not hotelid:
#         hotelid = request.session.create()
#     return hotelid

def hotels(request):
    
    allobject = Hotels.objects.all()
    context = {
        'allobject' : allobject
    }
    return render(request, "hotel.html", context)

def hotel(request, id):
    
    hotel = Hotels.objects.get(id=id)
    reviews = ReviewRating.objects.filter(status=True)
    
    data = {
        'hotel' : hotel,
        'reviews' : reviews,
    }
    
    return render(request, "single_hotel.html", data)

def submit_review(request, id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = ReviewRating()
            data.subject = form.cleaned_data['subject']
            data.rating = form.cleaned_data['rating']
            data.review = form.cleaned_data['review']
            data.ip = request.META.get('REMOTE_ADDR')
            data.id = id
            data.user_id = request.user.id
            data.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect('hotels')               
        
    else:
        return HttpResponse("fail")
    
def AddMarkedPlaces(request, id):
    addhotel = Hotels.objects.get(id=id)
    if request.user.is_authenticated:
        data = VisitLater()
        if VisitLater.objects.filter(hotel_name=addhotel.hotel_name).exists():
            pass
        else:
            data.hotel_name = addhotel.hotel_name
            data.location = addhotel.location
            data.save()
        
    return render(request, "accounts/profile.html")


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Restaurants, RestaurantReviewRating, VisitLaterR
from django.contrib import messages
from .forms import ReviewForm 

# Create your views here.

def restaurants(request):
    
    allobject = Restaurants.objects.all()
    context = {
        'allobject' : allobject
    }
    return render(request, "restaurant.html", context)

def restaurant(request, id):
    
    restaurant = Restaurants.objects.get(id=id)
    reviews = RestaurantReviewRating.objects.filter(status=True)
    data = {
        'restaurant' : restaurant,
        'reviews' : reviews
    }
    return render(request, "single_restaurant.html", data)


def submit_review(request, id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = RestaurantReviewRating()
            data.subject = form.cleaned_data['subject']
            data.rating = form.cleaned_data['rating']
            data.review = form.cleaned_data['review']
            data.ip = request.META.get('REMOTE_ADDR')
            data.id = id
            data.user_id = request.user.id
            data.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect('restaurants')               
        
    else:
        return HttpResponse("fail")
    
    
def AddMarkedPlacesR(request, id):
    addrestaurant = Restaurants.objects.get(id=id)
    if request.user.is_authenticated:
        data = VisitLaterR()
        if VisitLaterR.objects.filter(restaurant_name=addrestaurant.restaurant_name).exists():
            pass
        else:
            data.restaurant_name = addrestaurant.restaurant_name
            data.location = addrestaurant.location
            data.save()
        
    return render(request, "accounts/profile.html")
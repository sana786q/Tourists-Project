from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Temples, TempleReviewRating, VisitLaterT
from django.contrib import messages

# Create your views here.

def temples(request):
    
    allobject = Temples.objects.all()
    context = {
        'allobject' : allobject
    }
    return render(request, "temple.html", context)

def temple(request, id):
    
    temple = Temples.objects.get(id=id)
    reviews = TempleReviewRating.objects.filter(status=True)
    data = {
        'temple' : temple,
        'reviews' : reviews
    }
    return render(request, "single_temple.html", data)


def submit_review(request, id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = TempleReviewRating()
            data.subject = form.cleaned_data['subject']
            data.rating = form.cleaned_data['rating']
            data.review = form.cleaned_data['review']
            data.ip = request.META.get('REMOTE_ADDR')
            data.id = id
            data.user_id = request.user.id
            data.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect('temples')               
        
    else:
        return HttpResponse("fail")
    

def AddMarkedPlacesT(request, id):
    addtemple = Temples.objects.get(id=id)
    if request.user.is_authenticated:
        data = VisitLaterT()
        if VisitLaterT.objects.filter(temple_name=addtemple.temple_name).exists():
            pass
        else:
            data.temple_name = addtemple.temple_name
            data.location = addtemple.location
            data.save()
        
    return render(request, "accounts/profile.html")


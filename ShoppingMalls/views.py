from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ShoppingMalls, ShoppingMallReviewRating, VisitLaterS
from django.contrib import messages

# Create your views here.

def shoppingmalls(request):
    allobject = ShoppingMalls.objects.all()
    context = {
        'allobject' : allobject
    }
    return render(request, "shoppingmall.html", context)

def shoppingmall(request, id):
    
    shoppingmall = ShoppingMalls.objects.get(id=id)
    reviews = ShoppingMallReviewRating.objects.filter(status=True)
    data = {
        'shoppingmall' : shoppingmall,
        'reviews' : reviews
    }
    return render(request, "single_shopping_mall.html", data)


def submit_review(request, id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = ShoppingMallReviewRating()
            data.subject = form.cleaned_data['subject']
            data.rating = form.cleaned_data['rating']
            data.review = form.cleaned_data['review']
            data.ip = request.META.get('REMOTE_ADDR')
            data.id = id
            data.user_id = request.user.id
            data.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect('shoppingmalls')               
        
    else:
        return HttpResponse("fail")
    
def AddMarkedPlacesS(request, id):
    addmall = ShoppingMalls.objects.get(id=id)
    if request.user.is_authenticated:
        data = VisitLaterS()
        if VisitLaterS.objects.filter(mall_name=addmall.mall_name).exists():
            pass
        else:
            data.mall_name = addmall.mall_name
            data.location = addmall.location
            data.save()
        
    return render(request, "accounts/profile.html")



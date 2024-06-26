from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurants, name='restaurants'),
    path('<int:id>/', views.restaurant, name='restaurant'),
    path('submit_review/<int:id>/', views.submit_review, name='submit_review'),
    path('AddMarkedPlacesR/<int:id>/', views.AddMarkedPlacesR, name='AddMarkedPlacesR'),
]

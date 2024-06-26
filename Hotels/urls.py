from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotels, name='hotels'),
    path('<int:id>/', views.hotel, name='hotel'),
    path('submit_review/<int:id>/', views.submit_review, name='submit_review'),
    path('AddMarkedPlaces/<int:id>/', views.AddMarkedPlaces, name='AddMarkedPlaces'),
]

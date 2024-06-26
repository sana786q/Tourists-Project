from django.urls import path
from . import views

urlpatterns = [
    path('', views.temples, name='temples'),
    path('<int:id>/', views.temple, name='temple'),
    path('submit_review/<int:id>/', views.submit_review, name='submit_review'),
    path('AddMarkedPlacesT/<int:id>/', views.AddMarkedPlacesT, name='AddMarkedPlacesT'),
]

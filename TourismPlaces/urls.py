from django.urls import path
from . import views

urlpatterns = [
    path('', views.tourismplaces, name='tourismplaces'),
    path('<int:id>/', views.places, name='places'),
    path('submit_review/<int:id>/', views.submit_review, name='submit_review'),
    path('AddMarkedPlacesTP/<int:id>/', views.AddMarkedPlacesTP, name='AddMarkedPlacesTP'),
]

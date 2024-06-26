from django.urls import path
from . import views

urlpatterns = [
    path('', views.shoppingmalls, name='shoppingmalls'),
    path('<int:id>/', views.shoppingmall, name='shoppingmall'),
    path('submit_review/<int:id>/', views.submit_review, name='submit_review'),
    path('AddMarkedPlacesS/<int:id>/', views.AddMarkedPlacesS, name='AddMarkedPlacesS'),
]

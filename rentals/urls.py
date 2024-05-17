# rentals/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),  # Root path for the car list view
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('booking_confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
]

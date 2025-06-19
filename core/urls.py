from django.urls import path
from .views import BookingAPI

urlpatterns = [
    path('booking/',BookingAPI.as_view(),
name='booking-api')
]
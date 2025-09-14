from django.urls import path
from .views import index, bookings

urlpatterns = [
        path("", index),
        path("bookings", bookings)
]

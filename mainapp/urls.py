from django.urls import path
from .views import index, bookings, labours

urlpatterns = [
        path("", index),
        path("bookings", bookings),
        path("worker_<str:labr>", labours, name="app_user"),
]

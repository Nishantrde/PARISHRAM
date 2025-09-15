from django.urls import path
from .views import index, bookings, labours, assin_work

urlpatterns = [
        path("", index),
        path("bookings", bookings),
        path("worker_<str:labr>", labours, name="app_user"),
        path("assin_<str:labr>", assin_work, name="assin"),
]

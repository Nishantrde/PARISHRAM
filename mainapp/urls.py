from django.urls import path
from .views import index, bookings, labours, wait_labr, assin_work, wait_labr_tru_fla

app_name = 'mainapp'

urlpatterns = [
        path("", index, name="here"),
        path("bookings", bookings),
        path("worker_<str:labr>", labours, name="app_user"),
        path("assin_<str:labr>", assin_work, name="assin"),
        path("wrk_status_<str:labr>", wait_labr),
        path("wrk_<str:labr>", wait_labr_tru_fla, name="wait_labr_tru_fla")
]

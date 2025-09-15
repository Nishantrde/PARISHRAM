from django.shortcuts import render
from .models import Workers

# Create your views here.
def index(request):
    return render(request, "index.html")

def bookings(request):
    return render(request, "booking.html")

def labours(request, labr):
    worker_profile = Workers.objects.get(name = labr)
    print(worker_profile.name)
    profile = {"name":worker_profile.name, "occupation":worker_profile.occupation, "charge_per_hr":worker_profile.charge_per_hr, "ratings":worker_profile.ratings, "location":worker_profile.location}
    
    return render(request, "labr_index.html", profile)



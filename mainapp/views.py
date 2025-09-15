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
    profile = {"name":worker_profile.name, "occupation":worker_profile.occupation, "charge_per_hr":worker_profile.charge_per_hr, "ratings":worker_profile.ratings, "location":worker_profile.location, "on_work":worker_profile.on_work}
    
    return render(request, "labr_index.html", profile)

def assin_work(request, labr):
    print(labr,"here")
    worker_profile = Workers.objects.get(name = labr)
    worker_profile.on_work = True
    worker_profile.work_done = False
    worker_profile.save()
    profile = {"name":worker_profile.name, "occupation":worker_profile.occupation, "charge_per_hr":worker_profile.charge_per_hr, "ratings":worker_profile.ratings, "location":worker_profile.location, "on_work":worker_profile.on_work}

    return render(request, "labr_index.html", profile)

def wait_labr(request, labr):
    worker_profile = Workers.objects.get(name = labr)
    print(worker_profile.name, worker_profile.on_work)
    profile = {"name":worker_profile.name, "occupation":worker_profile.occupation, "charge_per_hr":worker_profile.charge_per_hr, "ratings":worker_profile.ratings, "location":worker_profile.location}
    
    return render(request, "wait_labr.html", profile)

def wait_labr_tru_fla(request, labr):
    worker_profile = Workers.objects.get(name = labr)
    print(worker_profile.name)
    profile = {"name":worker_profile.name, "occupation":worker_profile.occupation, "charge_per_hr":worker_profile.charge_per_hr, "ratings":worker_profile.ratings, "location":worker_profile.location, "on_work":worker_profile.on_work}
    
    if request.POST.get("decision") == "accept":
        print("accept")
        worker_profile.accept = True
        worker_profile.on_work = True
        worker_profile.work_done = False
        worker_profile.save()

    if request.POST.get("decision") == "reject":
        print("reject")
        worker_profile.accept = False
        worker_profile.on_work = False
        worker_profile.work_done = True
        worker_profile.save()
    
    if request.POST.get("decision") == "Done":
        print("Done")
        worker_profile.accept = False
        worker_profile.on_work = False
        worker_profile.work_done = True
        profile["on_work"] = worker_profile.on_work
        worker_profile.save()
        
        return render(request, "labr_index.html", profile)

    
    
    return render(request, "wait_labr.html", profile)



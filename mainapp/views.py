from django.shortcuts import render, redirect
from .models import Workers, User_profile


# Create your views here.
def index(request):
    usr_auth = False
    name = ""
    user_email = ""
    if request.user.is_authenticated:
        usr_auth = True
        # prefer first_name if non-empty, otherwise use email
        name = request.user.first_name if request.user.first_name else request.user.email
        user_email = request.user.email  # keep this as a plain string
        print(user_email, name)

        # get existing profile or create one (atomic and concise)
        profile, created = User_profile.objects.get_or_create(
            email=user_email,
            defaults={"name": name}
        )

        # optional: update name when profile exists but name changed
        if not created and profile.name != name:
            profile.name = name
            profile.save()

    return render(request, "index.html", {"usr_auth": usr_auth, "name": name, "email":user_email})


def my_bookings(request, usr):
    usr_profile = User_profile.objects.get(email = usr)
    print(usr_profile.history)
    wrk_lst = []
    for wrk in usr_profile.history:

        labr = Workers.objects.get(name = wrk)
        dit = {"name":labr.name, "occupation":labr.occupation, "charge_per_hr":labr.charge_per_hr, "location":labr.location}
        wrk_lst.append(dit)

    return render(request, "my_bookings.html", {"user_history":wrk_lst})


def bookings(request):
    print(request.user.first_name)
    return render(request, "booking.html", {"usr_name":request.user.first_name})

def labours(request, labr):
    worker_profile = Workers.objects.get(name = labr)
    print(worker_profile.name)
    print(request.user)
    profile = {"name":worker_profile.name, "occupation":worker_profile.occupation, "charge_per_hr":worker_profile.charge_per_hr, "ratings":worker_profile.ratings, "location":worker_profile.location, "on_work":worker_profile.on_work, "accept":worker_profile.accept}
    
    return render(request, "labr_index.html", profile)

def assin_work(request, labr):
    print(labr,"here123")
    worker_profile = Workers.objects.get(name = labr)
    worker_profile.on_work = True
    worker_profile.work_done = False
    worker_profile.save()
    print(worker_profile.accept, request.user.email)
    
    profile = {"name":worker_profile.name, "occupation":worker_profile.occupation, "charge_per_hr":worker_profile.charge_per_hr, "ratings":worker_profile.ratings, "location":worker_profile.location, "on_work":worker_profile.on_work, "accept":worker_profile.accept}

    return render(request, "labr_index.html", profile)

def wait_labr(request, labr):
    print(request.user.email)
    worker_profile = Workers.objects.get(name = labr)
    print(worker_profile.name, worker_profile.on_work)
    
    profile = {"name":worker_profile.name, "occupation":worker_profile.occupation, "charge_per_hr":worker_profile.charge_per_hr, "ratings":worker_profile.ratings, "location":worker_profile.location, "on_work":worker_profile.on_work, "accept":worker_profile.accept}
    
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
        
        print(request.user.email," -- ", User_profile.objects.filter(email=request.user.email))

        if User_profile.objects.filter(email=request.user.email).exists():
            usr = User_profile.objects.get(email=request.user.email)
            usr.history.append(worker_profile.name)
            usr.save()

        return render(request, "labr_index.html", profile)

    
    
    # return render(request, "wait_labr.html", profile)
    return redirect(f"/wrk_status_{labr}")



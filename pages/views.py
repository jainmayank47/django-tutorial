from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.
def home(request):
    teams = Team.objects.all()
    all_cars = Car.objects.order_by("id").filter(status=True)
    featured_cars= all_cars.filter(is_featured=True)
    model_search = Car.objects.values("model").distinct()
    body_style_search = Car.objects.values("body_style").distinct()
    year_search = Car.objects.values("year").distinct()
    city_search = Car.objects.values("city").distinct()
    data = {"teams":teams,
            "featured_cars":featured_cars,
            "all_cars":all_cars[:6],
            "model":model_search,
            "body_style":body_style_search,
            "year":year_search,
            "city":city_search
            }
    return render(request,"pages/home.html",data)

def about(request):
    teams = Team.objects.all()
    data = {"teams":teams}
    return render(request,"pages/about.html",data)

def cars(request):
    return render(request,"pages/cars.html")

def contact(request):
    return render(request,"pages/contact.html")

def services(request):
    return render(request,"pages/services.html")
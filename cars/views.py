from django.shortcuts import render
from .models import Car
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def cars(request):
    cars = Car.objects.order_by("id")
    paginator = Paginator(cars,4)
    page_no=request.GET.get("page")
    paged_cars=paginator.get_page(page_no)
    model_search = Car.objects.values("model").distinct()
    body_style_search = Car.objects.values("body_style").distinct()
    year_search = Car.objects.values("year").distinct()
    city_search = Car.objects.values("city").distinct()
    data  = {
        "cars":paged_cars,
        "model":model_search,
        "body_style":body_style_search,
        "year":year_search,
        "city":city_search
        
    }
    return render(request,"cars/cars.html",data)

def car_detail(request, id):
    car_detail = Car.objects.filter(id=id)
    features = str(car_detail[0].features)
    features = features.split(", ") 
    data  = {
        "car_detail":car_detail[0],
        "features":features
    }
    return render(request, "cars/car_detail.html",data)

def search(request):
    cars = Car.objects.all()
    print(cars)
    if request.GET.get("keyword"):
        keyword = request.GET.get("keyword")
        if keyword:
            cars= cars.filter(description__icontains=keyword)
    if request.GET.get("model"):
        model_no = request.GET.get("model")
        print(model_no)
        if model_no:
            cars = cars.filter(model__iexact=model_no)
    if request.GET.get("city"):
        city = request.GET.get("city")
        if city:
            cars = cars.filter(city=city)
    if request.GET.get("year"):
        year = request.GET.get("year")
        if year:
            cars = cars.filter(year=year)
    if request.GET.get("body_style"):
        body_style = request.GET.get("body_style")
        if body_style:
            cars = cars.filter(body_style=body_style)
    if request.GET.get("min_price"):
        min_price = request.GET.get("min_price")
        max_price = request.GET.get("max_price")
        if max_price:
            cars= cars.filter(price__gte=min_price,price__lte=max_price)
    model_search = Car.objects.values("model").distinct()
    body_style_search = Car.objects.values("body_style").distinct()
    year_search = Car.objects.values("year").distinct()
    city_search = Car.objects.values("city").distinct()
    data  = {
        "cars":cars,
        "model":model_search,
        "body_style":body_style_search,
        "year":year_search,
        "city":city_search
    }
    print(cars)
    return render(request,"cars/search.html",data)
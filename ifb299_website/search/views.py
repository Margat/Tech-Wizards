from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Car
from .forms import SearchForm
from django.shortcuts import redirect

# Create your views here.
# search bar
def home(request):
    title = "Home"
    if request.GET.get('query'):
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            min_price = form.cleaned_data['min_price']
            max_price = form.cleaned_data['max_price']
            all_cars = Car.objects.filter(car_make__icontains=query)
            all_cars = all_cars.filter(car_price_new__gte=min_price)
            all_cars = all_cars.filter(car_price_new__lte=max_price)
    else:
            all_cars = Car.objects.all()
            form = SearchForm()
    context = {
        'title': title,
        'form' : form,
        'all_cars' : all_cars
    }
    return render(request, 'search/home.html', context)

def car_detail(request, id):
    car = get_object_or_404(Car, pk=id)
    return HttpResponse("Details for car %s" % id)

def about(request):
    about = "About Us"
    context = {
        'title': about
        }
    return render(request, 'search/about.html', context)

def search(request):
    title = "Search"
    context = {
        'title': title
        }
    return render(request, 'search/search.html', context)

def locations(request):
    title = "Locations"
    context = {
        'title': title
        }
    return render(request, 'search/locations.html', context)

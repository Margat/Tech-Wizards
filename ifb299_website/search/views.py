from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Car
from .forms import SearchForm
from django.shortcuts import redirect

# Creates home page with form
def home(request):
    title = "Home"
    if request.GET.get('query'):
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            min_price = form.cleaned_data['min_price']
            max_price = form.cleaned_data['max_price']
            year = form.cleaned_data['year']
            all_cars = Car.objects.all()
            # If statements filter the results based on the inputs given
            if not(query == None):
                all_cars = all_cars.filter(car_make__icontains=query)
            else:
                print("Query: None")
            if not(min_price == None):
                all_cars = all_cars.filter(car_price_new__gte=min_price)
            else:
                print("Min_price: none")
            if not(max_price == None):
                all_cars = all_cars = all_cars.filter(car_price_new__lte=max_price)
            else:
                print("Min_price: none")
            if (year == 'None'):
                all_cars = all_cars.filter(car_series_year=year)
            else:
                print("Year field none")
    else:
            all_cars = Car.objects.all()
            form = SearchForm()
    # variables to be parsed to the html template        
    context = {
        'title': title,
        'form' : form,
        'all_cars' : all_cars
    }
    return render(request, 'search/home.html', context)


def car_detail(request, id):
    car = get_object_or_404(Car, pk=id)
    return HttpResponse("Details for car %s" % id)

# creates about page
def about(request):
    about = "About Us"
    context = {
        'title': about
        }
    return render(request, 'search/about.html', context)

# creates search page
def search(request):
    title = "Search"
    context = {
        'title': title
        }
    return render(request, 'search/search.html', context)

# creates request page
def locations(request):
    title = "Locations"
    context = {
        'title': title
        }
    return render(request, 'search/locations.html', context)

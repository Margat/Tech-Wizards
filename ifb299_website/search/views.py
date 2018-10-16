from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Car
from .forms import SearchForm
from django.shortcuts import render


# Creates home page with form
def home(request):
    title = "Home"
    form = SearchForm(request.GET)
    if form.is_valid():
        car_query_list = Car.objects.all()
        query = form.cleaned_data['query']
        min_price = form.cleaned_data['min_price']
        max_price = form.cleaned_data['max_price']
        year = form.cleaned_data['year']
        sort = form.cleaned_data['sort']
        if not min_price:
            min_price = 0
        if not max_price:
            max_price = 9999999
        car_query_list = car_query_list.filter(car_price_new__range=(min_price, max_price))
        if not query == None:
            car_query_list = car_query_list.filter(Q(car_make__icontains=query) | Q(car_model__icontains=query) | Q(car_series__icontains=query) | Q(car_body_type__icontains=query))
        if year != 'Blank':
            car_query_list = car_query_list.filter(car_series_year=year)
        if sort == 'ASC':
            car_query_list = car_query_list.order_by('car_price_new')
        if sort == 'DESC':
            car_query_list = car_query_list.order_by('-car_price_new')
    else:
            car_query_list = None
            form = SearchForm()
    context = {
        'title': title,
        'form' : form,
        'car_query_list' : car_query_list
    }
    return render(request, 'search/home.html', context)

def car_detail(request, id):
    selected_car = get_object_or_404(Car, pk=id)
    context = {
        'selected_car' : selected_car
    }
    return render(request, 'search/detail.html', context)

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

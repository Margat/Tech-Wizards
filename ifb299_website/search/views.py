from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Car, Store
from .forms import SearchForm
from django.shortcuts import render


# View to handle homepage requests
def home(request):
    title = "Home"
    form = SearchForm(request.GET) # Create bound SearchForm with form data submitted in GET request
    max_items = 21
    # If all form fields are valid, clean the data and begin filtering
    if form.is_valid():
        car_query_list = Car.objects.all()
        query = form.cleaned_data['query']
        min_price = form.cleaned_data['min_price']
        max_price = form.cleaned_data['max_price']
        year = form.cleaned_data['year']
        sort = form.cleaned_data['sort']
        # Check for empty fields and set defaults if necessary
        if not min_price:
            min_price = 0
        if not max_price:
            max_price = 9999999
        car_query_list = car_query_list.filter(car_price_new__range=(min_price, max_price))
        if not query == None:
            car_query_list = car_query_list.filter(Q(car_make__icontains=query) | Q(car_model__icontains=query) | Q(car_series__icontains=query) | Q(car_body_type__icontains=query))
        if year != 'Blank':
            year_max = 0
            if year.isdigit():
                year_max = int(year) + 9
            car_query_list = car_query_list.filter(car_series_year__range=(year, year_max))
        if sort == 'ASC':
            car_query_list = car_query_list.order_by('car_price_new')
        if sort == 'DESC':
            car_query_list = car_query_list.order_by('-car_price_new')
    # Create unbound SearchForm if form is not valid or is not submitted
    else:
            car_query_list = None
            form = SearchForm()
    context = {
        'title': title,
        'form' : form,
        'car_query_list' : car_query_list[0:max_items]
    }
    return render(request, 'search/home.html', context)

# View to handle car detail requests
def car_detail(request, id):
    # Get car based on its ID or return 404
    selected_car = get_object_or_404(Car, pk=id)
    context = {
        'selected_car' : selected_car
    }
    return render(request, 'search/detail.html', context)

# View to handle About Us page requests
def about(request):
    about = "About Us"
    context = {
        'title': about
        }
    return render(request, 'search/about.html', context)

# View to handle Locations page requests
def locations(request):
    title = "Locations"
    storeList = Store.objects.all()
    context = {
        'title': title,
        'storeList': storeList
        }
    return render(request, 'search/locations.html', context)

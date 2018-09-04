from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Car
from .forms import SearchForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            all_cars = Car.objects.filter(car_name__icontains=query)
            context = {
                'form' : form,
                'all_cars' : all_cars
            }

    else:
            all_cars = Car.objects.all()
            form = SearchForm()
            context = {
                'all_cars': all_cars,
                'form' : form
            }
    return render(request, 'search/home.html', context)

def car_detail(request, id):
    car = get_object_or_404(Car, pk=id)
    return HttpResponse("Details for car %s" % id)

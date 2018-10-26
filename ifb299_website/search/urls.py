from django.urls import path
from . import views

app_name = 'search'
urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:id>/', views.car_detail, name='car_detail'), # Passes parameter <int:id> (car.car_id) to dynamically create details page
    path('about/', views.about, name='about'),
    path('search/', views.about, name='search'),
    path('locations/', views.locations, name='locations'),
]

from django.urls import path
from . import views

app_name = 'search'
urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:id>/', views.car_detail, name='car_detail'),
    path('about/', views.about, name='about'),
    path('search/', views.about, name='search'),
    path('locations/', views.about, name='locations'),
]

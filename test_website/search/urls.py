from django.urls import path
from . import views

app_name = 'search'
urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:id>/', views.car_detail, name='car_detail'),
]

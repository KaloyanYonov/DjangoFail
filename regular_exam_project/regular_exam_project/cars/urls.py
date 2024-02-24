from django.urls import path
from . import views

urlpatterns = [
    path('catalogue/', views.car_catalogue, name='car_catalogue'),
    path('create/', views.car_create, name='car_create'),
    path('<int:id>/details/', views.car_details, name='car_details'),
    path('<int:id>/edit/', views.car_edit, name='car_edit'),
    path('<int:id>/delete/', views.car_delete, name='car_delete'),
]


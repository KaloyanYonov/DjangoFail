from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('create/', views.profile_create, name='profile_create'),
    path('details/', views.profile_details, name='profile_details'),
    path('edit/', views.profile_edit, name='profile_edit'),
    path('delete/', views.profile_delete, name='profile_delete'),
]

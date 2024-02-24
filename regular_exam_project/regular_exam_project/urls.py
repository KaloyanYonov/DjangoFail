from django.urls import path, include

from regular_exam_project.cars import views
from regular_exam_project.cars.views import car_catalogue

urlpatterns = [
    path('', include('regular_exam_project.web.urls')),
    path('car/', include('regular_exam_project.cars.urls')),
    path('profile/', include('regular_exam_project.profiles.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

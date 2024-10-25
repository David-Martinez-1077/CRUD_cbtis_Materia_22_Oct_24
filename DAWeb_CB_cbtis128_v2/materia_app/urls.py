from django.urls import path
from materia_app import views

urlpatterns = [
    path('', views.inicio_Vista, name="views.inicio_vista")
]

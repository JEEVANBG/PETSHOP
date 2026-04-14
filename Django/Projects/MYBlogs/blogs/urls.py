from django.urls import path
from yarl import URL
from . import views

urlpatterns = [
    path('', views.home),
]
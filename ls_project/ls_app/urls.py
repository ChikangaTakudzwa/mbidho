from django.urls import path
""" URLS """
from . import views

urlpatterns = [
  path('', views.index, name='index'),
]

from django.urls import path
from . import views

# root: /products

urlpatterns = [
    path('', views.index),
    path('new', views.new),
]



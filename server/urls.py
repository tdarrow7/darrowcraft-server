from django.contrib import admin
from django.urls import path
from server import views

urlpatterns = [
    path('coffee/', views.CoffeeList.as_view(), name='coffee_list'),
    path('coffee-details/<int:pk>', views.CoffeeDetails.as_view(), name='coffee_detail'),
]

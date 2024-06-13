from django.contrib import admin
from django.urls import path
from server import views

urlpatterns = [
    path('coffee/', views.CoffeeList.as_view(), name='coffee_list'),
    path('coffee-details/<int:pk>', views.CoffeeDetails.as_view(), name='coffee_detail'),
    path('roast-types', views.RoastTypeList.as_view(), name='roast_type_list'),
    path('roast-types/<int:pk>', views.RoastTypeDetails.as_view(), name="roast_type_detail"),
    path('brands/', views.BrandList.as_view(), name='brand_list'),
    path('brand-details/<int:pk>', views.BrandDetails.as_view(), name="brand_detail"),
    # path('roast-types/<slug:slug>/', RoastTypeDetails.as_view(), name="roast_type_detail"),
]

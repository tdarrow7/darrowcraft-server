from django.shortcuts import render
from rest_framework import generics, permissions, viewsets

from .serializers import CoffeeSerializer, BrandSerializer, RoastTypeSerializer
from .models import Coffee, Brand, RoastType
# Create your views here.

class CoffeeList(generics.ListCreateAPIView):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer

# Fix this, todd broke it
class CoffeeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer

class BrandList(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

# Fix this, todd broke it
class BrandDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class RoastTypeList(generics.ListCreateAPIView):
    queryset = RoastType.objects.all()
    serializer_class = RoastTypeSerializer

# Fix this, todd broke it
class RoastTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoastType.objects.all()
    serializer_class = RoastTypeSerializer
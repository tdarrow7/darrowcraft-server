from rest_framework import serializers
from .models import Coffee, RoastType, Brand

class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = ('id', 'type','isGround', 'dateAdded', 'description')

class RoastTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoastType
        fields = ('id', 'name')

class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Brand
        fields = ('id', 'name', 'coffee')
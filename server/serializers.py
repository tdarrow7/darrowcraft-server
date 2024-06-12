from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Coffee, RoastType, Brand

class CoffeeSerializer(ModelSerializer):
    class Meta:
        model = Coffee
        fields = ('id', 'type','isGround', 'dateAdded', 'description')

class RoastTypeSerializer(ModelSerializer):
    class Meta:
        model = RoastType
        fields = ('id', 'name')

class BrandSerializer(HyperlinkedModelSerializer):
    class Meta: 
        model = Brand
        fields = ('id', 'name', 'coffee')
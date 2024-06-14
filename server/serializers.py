from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Coffee, RoastType, Brand

class CoffeeSerializer(ModelSerializer):
    class Meta:
        model = Coffee
        fields = ('id', 'type','isGround', 'dateAdded', 'description', 'brand', 'roast')

class RoastTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = RoastType
        fields = ['id', 'name']  

class BrandSerializer(ModelSerializer):
    class Meta: 
        model = Brand
        fields = ('id', 'name', 'description')
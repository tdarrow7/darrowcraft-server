from django.db import models
from django.db.models.fields import CharField, AutoField, BooleanField

# Create your models here.
class Coffee(models.Model): 
    id = AutoField(primary_key=True)
    type = CharField(max_length=36)
    isGround = BooleanField()
    dateAdded = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=128)
    # roastType = models.ForeignKey(RoastType, to_field='id')
    # brandID = models.ForeignKey(Brand, to_field=id)

class RoastType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=36)

class Brand(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=36)
    # coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE, related_name='brands')

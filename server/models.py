from django.db import models
from django.db.models.fields import CharField, AutoField, BooleanField

# Create your models here.

class Brand(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=36)
    description = models.CharField(max_length=1024, null=True)
    dateAdded = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name

class Coffee(models.Model): 
    id = AutoField(primary_key=True)
    type = CharField(max_length=36)
    isGround = BooleanField()
    dateAdded = models.DateTimeField(auto_now=True)
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE, related_name='coffees')
    roastType = models.ForeignKey("RoastType", on_delete=models.CASCADE, related_name='coffees')
    description = models.TextField(max_length=128)

class RoastType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=36)
    def __str__(self) -> str:
        return self.name



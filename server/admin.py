from django.contrib import admin
from .models import Coffee, Brand, RoastType

admin.site.register(Coffee)
admin.site.register(Brand)
admin.site.register(RoastType)
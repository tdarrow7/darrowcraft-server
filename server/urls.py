from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static
# f import 
from server import views

from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('coffee/', views.CoffeeList.as_view(), name='coffee_list'),
    path('coffee-details/<int:pk>', views.CoffeeDetails.as_view(), name='coffee_detail'),
    path('roast-types/', views.RoastTypeList.as_view(), name='roast_type_list'),
    path('roast-types/<int:pk>', views.RoastTypeDetails.as_view(), name="roast_type_detail"),
    # path('roast-types/<slug:slug>/', views.RoastTypeDetails.as_view(), name="roast_type_detail",),
    path('brands/', views.BrandList.as_view(), name='brand_list'),
    path('brand-details/<int:pk>', views.BrandDetails.as_view(), name="brand_detail"),
]

# add at the last
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

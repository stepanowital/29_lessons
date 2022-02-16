from simple_serializer.views import StoreViewSet
from django.urls import path, include
from rest_framework import routers

simple_router = routers.SimpleRouter()
simple_router.register("simple_serializer", StoreViewSet, basename="simple serializer")

urlpatterns = [
    path("", include(simple_router.urls))
]

from fk_serializer.views import StoreViewSet
from django.urls import path, include
from rest_framework import routers

simple_router = routers.SimpleRouter()
simple_router.register("fk_serializer", StoreViewSet, basename="fk serializer")

urlpatterns = [
    path("", include(simple_router.urls))
]

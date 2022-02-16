from m2m_serializer.views import StoreViewSet
from django.urls import path, include
from rest_framework import routers

simple_router = routers.SimpleRouter()
simple_router.register("m2m_serializer", StoreViewSet, basename="fk serializer")

urlpatterns = [
    path("", include(simple_router.urls))
]

from rest_framework import routers
from django.urls import path, include

from router import views

simple_router = routers.SimpleRouter()
simple_router.register('router_stores', views.StoreViewSet)

urlpatterns = [
   path('', include(simple_router.urls))
]

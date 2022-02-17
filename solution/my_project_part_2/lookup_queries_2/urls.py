from rest_framework import routers
from django.urls import path, include

from lookup_queries_2 import views

simple_router = routers.SimpleRouter()
simple_router.register('lookup_queries_2', views.StoreViewSet)

urlpatterns = [
   path('', include(simple_router.urls))
]

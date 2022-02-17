from rest_framework import routers
from django.urls import path, include

from qf_queries import views

simple_router = routers.SimpleRouter()
simple_router.register('qf_queries', views.StoreViewSet)

urlpatterns = [
   path('', include(simple_router.urls))
]

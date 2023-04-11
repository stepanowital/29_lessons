# TODO здесь необходимо настроить urls приложения
from django.urls import path, include
from rest_framework import routers

from qf_queries import views

simple_router = routers.SimpleRouter()
simple_router.register('qf_queries', views.StoreView)

urlpatterns = [
   path('', include(simple_router.urls))
]

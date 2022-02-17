from rest_framework import routers
from django.urls import path, include

from fk_search import views

simple_router = routers.SimpleRouter()
simple_router.register('fk_search', views.StoreViewSet)

urlpatterns = [
   path('', include(simple_router.urls))
]

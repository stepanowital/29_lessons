# TODO опишите view-функцию ниже
from rest_framework.viewsets import ModelViewSet

from lookup_queries.models import Store
from lookup_queries.serializers import StoreSerializer


class StoreView(ModelViewSet):
    queryset = Store.objects.filter(name__icontains="пят")
    serializer_class = StoreSerializer

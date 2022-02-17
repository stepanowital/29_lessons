from rest_framework import viewsets

from lookup_queries.serializers import StoreSerializer
from lookup_queries.models import Store


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.filter(name__icontains="пят")


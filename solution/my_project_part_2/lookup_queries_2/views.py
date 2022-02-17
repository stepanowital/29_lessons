from rest_framework import viewsets

from lookup_queries_2.serializers import StoreSerializer
from lookup_queries_2.models import Store


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.filter(address__endswith="д. 30")

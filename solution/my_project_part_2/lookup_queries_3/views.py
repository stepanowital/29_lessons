from rest_framework import viewsets

from lookup_queries_3.serializers import StoreSerializer
from lookup_queries_3.models import Store


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.filter(open_hour__range=[8, 10])

# TODO опишите view-функцию ниже
from rest_framework.viewsets import ModelViewSet

from lookup_queries_2.models import Store
from lookup_queries_2.serializers import StoreSerializer


class StoreView(ModelViewSet):
    queryset = Store.objects.filter(address__endswith="д. 30")
    serializer_class = StoreSerializer

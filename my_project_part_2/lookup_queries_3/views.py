# TODO опишите view-функцию ниже
from rest_framework.viewsets import ModelViewSet

from lookup_queries_3.models import Store
from lookup_queries_3.serializers import StoreSerializer


class StoreView(ModelViewSet):
    queryset = Store.objects.filter(open_hour__range=[8, 10])
    serializer_class = StoreSerializer

# TODO опишите view-функцию ниже
from rest_framework.viewsets import ModelViewSet

from fk_search.models import Store
from fk_search.serializers import StoreSerializer


class StoreView(ModelViewSet):
    queryset = Store.objects.filter(city__name__icontains="Самара")
    serializer_class = StoreSerializer

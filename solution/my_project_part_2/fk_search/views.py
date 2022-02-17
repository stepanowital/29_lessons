from rest_framework import viewsets

from fk_search.serializers import StoreSerializer
from fk_search.models import Store


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

    def get_queryset(self):
        return Store.objects.filter(
            city__name='Самара'
        )

from rest_framework import viewsets

from router.serializers import StoreSerializer
from router.models import Store


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

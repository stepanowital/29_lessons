from rest_framework.viewsets import ModelViewSet

from simple_serializer.serializers import StoreSerializer
from simple_serializer.models import Store


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

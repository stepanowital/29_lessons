from rest_framework.viewsets import ModelViewSet

from fk_serializer.serializers import StoreSerializer
from fk_serializer.models import Store


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

from rest_framework.viewsets import ModelViewSet

from m2m_serializer.serializers import StoreSerializer
from m2m_serializer.models import Store


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

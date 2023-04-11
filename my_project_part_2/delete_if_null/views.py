# TODO опишите view-функцию ниже
from rest_framework.viewsets import ModelViewSet

from delete_if_null.models import Store
from delete_if_null.serializers import StoreSerializer


class StoreView(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def get_queryset(self):
        Store.objects.filter(visits=0).delete()

        return super().get_queryset()

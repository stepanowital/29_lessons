from rest_framework import generics

from retrieve_view.models import Store
from retrieve_view.serializers import StoreSerializer


# TODO опишите RetrieveView ниже
class StoreRetrieveView(generics.RetrieveAPIView):
    queryset = Store.objects.all()

    serializer_class = StoreSerializer

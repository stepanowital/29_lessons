from rest_framework import generics

from retrieve_view.serializers import StoreSerializer
from retrieve_view.models import Store


class StoreRetrieveView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


from rest_framework import generics

from slug_retrieve_view.serializers import StoreSerializer
from slug_retrieve_view.models import Store


class StoreRetrieveView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    lookup_field = 'slug'

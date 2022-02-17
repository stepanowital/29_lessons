from rest_framework import generics

from delete_if_null.serializers import StoreSerializer
from delete_if_null.models import Store


class StoreListView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def get_queryset(self):
        Store.objects.filter(visits=0).delete()

        return super().get_queryset()

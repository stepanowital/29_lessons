from rest_framework import generics

from update_view.models import Store
from update_view.serializers import StoreSerializer


# TODO опишите UpdateView здесь
class StoreUpdateView(generics.UpdateAPIView):
    queryset = Store.objects.all()

    serializer_class = StoreSerializer

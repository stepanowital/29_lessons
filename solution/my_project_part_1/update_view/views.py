from rest_framework import generics

from update_view .serializers import StoreSerializer
from update_view.models import Store


class StoreUpdateView(generics.UpdateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

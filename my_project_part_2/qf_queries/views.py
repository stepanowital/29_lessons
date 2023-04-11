# TODO опишите view-функцию ниже
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet

from qf_queries.models import Store
from qf_queries.serializers import StoreSerializer


class StoreView(ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.filter(
        Q(email__icontains="ivan") |
        Q(director__icontains="ivan")
    )

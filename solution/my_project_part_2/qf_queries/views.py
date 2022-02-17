from django.db.models import Q
from rest_framework import viewsets

from qf_queries.models import Store
from qf_queries.serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.filter(
             Q(email__icontains="ivan") |
             Q(director__icontains="ivan")
    )

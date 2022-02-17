from fk_search.models import Store, City
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Store
        fields = "__all__"

from rest_framework import serializers

from fk_serializer.models import Store, City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Store
        fields = '__all__'

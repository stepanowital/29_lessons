from rest_framework import serializers

from simple_serializer.models import Store


# TODO опишите сериалайзер ниже
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

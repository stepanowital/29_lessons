from rest_framework import serializers

from m2m_serializer.models import Store, City, WorkHours


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class WorkHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHours
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    work_hours = WorkHoursSerializer(many=True)

    class Meta:
        model = Store
        fields = '__all__'

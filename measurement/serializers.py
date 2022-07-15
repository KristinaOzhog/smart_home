from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from measurement.models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'


class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = '__all__'


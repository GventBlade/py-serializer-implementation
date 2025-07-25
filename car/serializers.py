from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    model = serializers.CharField(required=True, max_length=64)
    horse_powers = serializers.IntegerField(min_value=1, max_value=1914)
    is_broken = serializers.BooleanField(required=True)
    problem_description = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = Car
        fields = ('id', 'model', 'horse_powers', 'is_broken', 'problem_description')

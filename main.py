import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    serializer_data = serializer.data
    json_output = json.dumps(serializer_data)


def deserialize_car_object(json: bytes) -> Car:
    json_string = json.decode("utf-8")
    data_dict = json.loads(json_string)
    serializer = CarSerializer(data=data_dict)
    serializer.is_valid(raise_exception=True)
    return serializer.save()

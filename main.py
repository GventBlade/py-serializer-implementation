import json as json_module

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    serializer_data = serializer.data
    json_string = json_module.dumps(serializer_data, separators=(',', ':'))
    json_output_bytes = json_string.encode("utf-8")
    return json_output_bytes


def deserialize_car_object(json: bytes) -> Car:
    json_string = json.decode("utf-8")
    data_dict = json_module.loads(json_string)
    serializer = CarSerializer(data=data_dict)
    serializer.is_valid(raise_exception=True)
    car_instance = serializer.save()
    return car_instance

from rest_framework import viewsets
from rest_framework.response import Response

from core.models import Car
from core.api.car.serializer import (
    CarSerializer,
)
import json


class CarViewset(viewsets.ModelViewSet):
    """
    This Viewset is for Car API. Here we can add any description.
    """
    serializer_class = CarSerializer
    queryset = Car.objects.all()

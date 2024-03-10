from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from .models import Race, Racer, Car, Result
from .seriializers import (RaceSerializer, RacerSerializer, CarSerializer, CarGetSerializer, ResultGetSerializer,
                           ResultSerializer)


@extend_schema(description="This section contains operations related to Race.", tags=["Race"])
class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer


@extend_schema(description="This section contains operations related to Racer.", tags=["Racer"])
class RacerViewSet(viewsets.ModelViewSet):
    queryset = Racer.objects.all()
    serializer_class = RacerSerializer


@extend_schema(description="This section contains operations related to Car.", tags=["Car"])
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CarGetSerializer
        return CarSerializer


@extend_schema(description="This section contains operations related to Result.", tags=["Result"])
class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ResultGetSerializer
        return ResultSerializer

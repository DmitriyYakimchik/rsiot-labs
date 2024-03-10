from rest_framework import serializers
from .models import Race, Racer, Car, Result


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'


class RacerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Racer
        fields = '__all__'


class CarGetSerializer(serializers.ModelSerializer):
    racer = RacerSerializer()

    class Meta:
        model = Car
        fields = ['id', 'racer', 'brand', 'model', 'number']


class CarSerializer(serializers.ModelSerializer):
    racer = serializers.PrimaryKeyRelatedField(queryset=Racer.objects.all())

    class Meta:
        model = Car
        fields = ['id', 'racer', 'brand', 'model', 'number']


class ResultGetSerializer(serializers.ModelSerializer):
    race = RaceSerializer()
    racer = RacerSerializer()
    car = CarSerializer()

    class Meta:
        model = Result
        fields = ['id', 'race', 'racer', 'car', 'time', 'position']

class ResultSerializer(serializers.ModelSerializer):
    race = serializers.PrimaryKeyRelatedField(queryset=Race.objects.all())
    racer = serializers.PrimaryKeyRelatedField(queryset=Racer.objects.all())
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())
    time = serializers.DurationField()

    class Meta:
        model = Result
        fields = ['id', 'race', 'racer', 'car', 'time', 'position']

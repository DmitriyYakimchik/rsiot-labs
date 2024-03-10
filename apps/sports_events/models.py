from django.db import models


class Race(models.Model):
    """Модель для гоночного события"""
    name = models.CharField(max_length=100)  # Название гонки
    date = models.DateField()  # Дата проведения
    location = models.CharField(max_length=200)  # Место проведения
    distance = models.FloatField()  # Дистанция в километрах

    def __str__(self):
        return self.name


class Racer(models.Model):
    """Модель для участника гонки"""
    name = models.CharField(max_length=100) # Имя участника
    date_of_birth = models.DateField() # Возраст участника

    def __str__(self):
        return self.name


class Car(models.Model):
    # Модель для автомобиля участника
    racer = models.OneToOneField(Racer, on_delete=models.CASCADE) # Ссылка на участника
    brand = models.CharField(max_length=50) # Марка автомобиля
    model = models.CharField(max_length=50) # Модель автомобиля
    number = models.CharField(max_length=10) # Номер автомобиля

    def __str__(self):
        return f'{self.brand} {self.model} - {self.number}'


class Result(models.Model):
    """Модель для результата гонки"""
    race = models.ForeignKey(Race, on_delete=models.CASCADE)  # Ссылка на гонку
    racer = models.ForeignKey(Racer, on_delete=models.CASCADE)  # Ссылка на участника
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    time = models.DurationField()  # Время, затраченное на гонку
    position = models.PositiveIntegerField()  # Место, занятое в гонке

    def __str__(self):
        return f'{self.racer} - {self.race} - {self.time}'

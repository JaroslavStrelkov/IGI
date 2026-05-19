from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CarCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):

    TRANSMISSION_CHOICES = (('manual', 'Механика'), ('automatic', 'Автомат'))
    FUEL_CHOICES = (('petrol', 'Бензин'), ('diesel', 'Дизель'), ('electric', 'Электро'), ('hybrid', 'Гибрид'))
    category = models.ForeignKey(CarCategory, on_delete=models.CASCADE, related_name='cars')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='cars')
    features = models.ManyToManyField(Feature, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    image = models.ImageField(upload_to='cars/')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
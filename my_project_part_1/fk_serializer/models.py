from django.db import models


class City(models.Model):
    name = models.CharField(max_length=10)


class Store(models.Model):
    slug = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=14, decimal_places=6)
    longitude = models.DecimalField(max_digits=14, decimal_places=6)
    email = models.EmailField(max_length=30)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

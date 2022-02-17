from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    open_hour = models.SmallIntegerField()
    close_hour = models.SmallIntegerField()
    email = models.EmailField()
    director = models.CharField(max_length=100)

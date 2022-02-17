from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

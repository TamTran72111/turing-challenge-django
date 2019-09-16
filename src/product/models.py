from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=150, null=True)
    image_2 = models.CharField(max_length=150, null=True)
    thumbnail = models.CharField(max_length=150, null=True)
    display = models.SmallIntegerField()

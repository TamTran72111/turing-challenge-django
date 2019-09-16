from django.db import models


class ShippingRegion(models.Model):
    shipping_region = models.CharField(max_length=100)

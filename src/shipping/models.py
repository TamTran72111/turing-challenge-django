from django.db import models

from shippingRegion.models import ShippingRegion


class Shipping(models.Model):
    shipping_type = models.CharField(max_length=100)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_region = models.ForeignKey(
        ShippingRegion, on_delete=models.CASCADE)

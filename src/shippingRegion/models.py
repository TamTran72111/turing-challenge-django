from django.db import models


class ShippingRegion(models.Model):
    shipping_region = models.CharField(max_length=100)

    def __str__(self):
        return f'<Shipping Region: {self.shipping_region}>'

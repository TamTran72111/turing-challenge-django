from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from shippingRegion.models import ShippingRegion


class Customer(AbstractUser):
    email = models.EmailField(
        _('email address'),
        max_length=100, unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        }
    )
    credit_card = models.TextField(null=True)
    address_1 = models.CharField(max_length=100, null=True)
    address_2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=100, null=True)
    postal_code = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    shipping_region = models.ForeignKey(
        ShippingRegion, on_delete=models.CASCADE)
    day_phone = models.CharField(max_length=100, null=True)
    eve_phone = models.CharField(max_length=100, null=True)
    mob_phone = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.username

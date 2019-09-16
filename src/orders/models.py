from django.db import models

from customer.models import Customer
from shipping.models import Shipping
from tax.models import Tax


class Orders(models.Model):
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    created_on = models.DateTimeField(auto_now_add=True)
    shipped_on = models.DateTimeField(null=True)
    status = models.IntegerField(default=0)
    comments = models.CharField(max_length=255, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    auth_code = models.CharField(max_length=50, null=True)
    reference = models.CharField(max_length=50, null=True)
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE)
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE)

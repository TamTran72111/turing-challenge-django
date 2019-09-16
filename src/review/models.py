from django.db import models

from customer.models import Customer
from product.models import Product


class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.SmallIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

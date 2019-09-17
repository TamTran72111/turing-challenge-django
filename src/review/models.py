from django.db import models

from customer.models import Customer
from product.models import Product


class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='reviews', on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.SmallIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'<Review of {self.customer.username} for {self.product.name}>'

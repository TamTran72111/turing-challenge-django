from django.db import models

from orders.models import Orders
from product.models import Product


class OrderDetail(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attributes = models.CharField(max_length=1000)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    uni_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'<Product {self.product.name} of order #{self.order.id}'

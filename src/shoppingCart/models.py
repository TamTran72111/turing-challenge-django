from django.db import models

from product.models import Product


class ShoppingCart(models.Model):
    cart_id = models.CharField(max_length=32)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attributes = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    buy_now = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'<Shopping cart: {self.cart_id}>'

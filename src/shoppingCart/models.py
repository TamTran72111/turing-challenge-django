from django.db import models

from product.models import Product
from utils import get_object_or_404, get_list_or_404


class ShoppingCart(models.Model):
    cart_id = models.UUIDField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attributes = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    buy_now = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'<Shopping cart: {self.cart_id}>'

    @classmethod
    def add_to_cart(cls, data):
        cart_id = data.get('cart_id')
        product_id = data.get('product').get('id')
        attributes = data.get('attributes')

        product = get_object_or_404(Product, id=product_id)
        cart, _ = ShoppingCart.objects.get_or_create(cart_id=cart_id,
                                                     product=product,
                                                     attributes=attributes,
                                                     defaults={'quantity': 0}
                                                     )
        cart.quantity += 1
        cart.save()

        return cart

    @classmethod
    def get_total_amount(cls, cart_id):
        items = get_list_or_404(ShoppingCart, cart_id=cart_id)
        return sum([item.quantity * item.product.price for item in items])

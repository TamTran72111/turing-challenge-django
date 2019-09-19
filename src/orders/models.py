from django.db import models

from customer.models import Customer
from tax.models import Tax
from shipping.models import Shipping
from shoppingCart.models import ShoppingCart


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

    def __str__(self):
        return f'<Order {self.id} on {self.created_on}'

    def add_details(self, cart_id):
        cart_items = ShoppingCart.objects.filter(cart_id=cart_id)
        for cart_item in cart_items:
            self.orderdetail_set.create(
                **(self.__get_orderDetail_dict(cart_item)))
        for cart_item in cart_items:
            cart_item.delete()

    def __get_orderDetail_dict(self, cart_item):
        return {
            'order': self,
            'product': cart_item.product, 'attributes': cart_item.attributes,
            'product_name': cart_item.product.name, 'quantity': cart_item.quantity,
            'unit_cost': cart_item.product.price
        }

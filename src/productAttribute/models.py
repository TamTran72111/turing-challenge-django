from django.db import models

from attributeValue.models import AttributeValue
from product.models import Product


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute_value = models.ForeignKey(
        AttributeValue,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('product', 'attribute_value')

    def __str__(self):
        return f'<Product {self.product.name}' \
            f' - Attribute: {self.attribute_value.value}>'

from django.db import models

from attributeValue.models import AttributeValue
from product.models import Product
from utils import get_list_or_404


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

    @classmethod
    def get_attribute_values_from_product_id(cls, product_id):
        product_attributes = get_list_or_404(cls, product__id=product_id)
        return [pa.attribute_value for pa in product_attributes]

from django.db import models

from category.models import Category
from product.models import Product


class ProductCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('category', 'product')

    def __str__(self):
        return f'<Product {self.product.name} ' \
            f'- Category: {self.category.name}>'

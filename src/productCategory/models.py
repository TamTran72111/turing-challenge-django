from django.db import models

from utils import get_list_or_404
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

    @classmethod
    def get_categories_from_product_id(cls, product_id):
        productCategories = get_list_or_404(cls, product__id=product_id)
        print(productCategories)
        categories = [pc.category for pc in productCategories]
        print(categories)
        return categories

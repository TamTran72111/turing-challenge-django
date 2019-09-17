from django.db import models

from utils import get_list_or_404, get_object_or_404
from category.models import Category
from department.models import Department
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
        return [pc.category for pc in productCategories]

    @classmethod
    def get_products_from_category_id(cls, category_id):
        productCategories = get_list_or_404(cls, category__id=category_id)
        return [pc.product for pc in productCategories]

    @classmethod
    def get_products_from_department_id(cls, department_id):
        department = get_object_or_404(Department, id=department_id)
        categories = department.categories.all()
        productCategories = get_list_or_404(cls, category__in=categories)
        return [pc.product for pc in productCategories]

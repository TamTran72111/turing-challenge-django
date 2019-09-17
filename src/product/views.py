from collections import OrderedDict

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from category.serializers import ProductLocationSerializer
from productCategory.models import ProductCategory
from review.serializers import ReviewSerializer
from .models import Product
from .serializers import SingleProductSerializer, ProductsSerializer


class ProductList(ListAPIView):
    serializer_class = ProductsSerializer


class ProductListView(ProductList):
    queryset = Product.objects.all()


class ProductView(RetrieveAPIView):
    serializer_class = SingleProductSerializer
    queryset = Product.objects.all()


class ProductInCategoryView(ProductList):
    def get_queryset(self):
        return ProductCategory.get_products_from_category_id(self.kwargs.get('id'))


class ProductInDepartmentView(ProductList):
    def get_queryset(self):
        return ProductCategory.get_products_from_department_id(self.kwargs.get('id'))


class ProductLocationView(ListAPIView):
    serializer_class = ProductLocationSerializer

    def get_queryset(self):
        return ProductCategory.get_categories_from_product_id(self.kwargs.get('id'))


class ProductReviewView(ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Product.get_reviews_from_id(self.kwargs.get('id'))

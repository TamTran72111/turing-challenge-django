from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.viewsets import ReadOnlyModelViewSet

from department.models import Department
from productCategory.models import ProductCategory
from .models import Category
from .serializers import CategorySerializer


class CategoryViewset(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductCategoryView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return ProductCategory.get_categories_from_product_id(
            self.kwargs.get('id'))


class DepartmentCategoryView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Department.get_categories_from_id(self.kwargs.get('id'))

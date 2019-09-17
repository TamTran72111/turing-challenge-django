from django.urls import path, include

from .views import ProductView, ProductListView, ProductInCategoryView
from .views import ProductInDepartmentView, ProductLocationView
from .views import ProductReviewView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:pk>', ProductView.as_view(), name='product-item'),
    path('inCategory/<int:id>', ProductInCategoryView.as_view(),
         name='product-in-category'),
    path('inDepartment/<int:id>', ProductInDepartmentView.as_view(),
         name='products-in-department'),
    path('<int:id>/locations', ProductLocationView.as_view(),
         name='product-locations'),
    path('<int:id>/reviews', ProductReviewView.as_view(),
         name='product-reviews'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewset, ProductCategoryView, DepartmentCategoryView

router = DefaultRouter()
router.register('', CategoryViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('inDepartment/<int:id>', DepartmentCategoryView.as_view()),
    path('inProduct/<int:id>', ProductCategoryView.as_view()),
]

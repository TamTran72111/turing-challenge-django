from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AttributeViewset, AttributeValueView, ProductAttributeView

router = DefaultRouter()
router.register('', AttributeViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('values/<int:id>', AttributeValueView.as_view()),
    path('inProduct/<int:id>', ProductAttributeView.as_view()),
]

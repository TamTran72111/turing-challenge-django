from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TaxViewset

router = DefaultRouter()
router.register('', TaxViewset)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include

from .views import ShippingView, ShippingRegionView


urlpatterns = [
    path('', ShippingRegionView.as_view()),
    path('<int:region_id>', ShippingView.as_view()),
]

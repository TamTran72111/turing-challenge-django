from django.urls import path

from .views import CreateOrdersView, OrderDetailView, OrderInCustomerView

urlpatterns = [
    path('', CreateOrdersView.as_view()),
    path('<int:id>', OrderDetailView.as_view()),
    path('inCustomer', OrderInCustomerView.as_view()),
]

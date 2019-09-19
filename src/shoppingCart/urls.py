from django.urls import path

from .views import GenerateUUIDView, ShoppingCartView, AddToCartView
from .views import UpdateCartItemView, DeleteCartView, RemoveItemView
from .views import TotalAmountView

urlpatterns = [
    path('generateUniqueId', GenerateUUIDView.as_view()),
    path('add', AddToCartView.as_view()),
    path('<str:cart_id>', ShoppingCartView.as_view()),
    path('update/<int:id>', UpdateCartItemView.as_view()),
    path('empty/<str:cart_id>', DeleteCartView.as_view()),
    path('removeItem/<int:item_id>', RemoveItemView.as_view()),
    path('totalAmount/<str:cart_id>', TotalAmountView.as_view()),
]

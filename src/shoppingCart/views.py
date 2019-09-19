import uuid

from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.generics import UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from utils import get_list_or_404, get_object_or_404
from .models import ShoppingCart
from .serializers import ShoppingCartSerializer, UpdateCartSerializer


class GenerateUUIDView(APIView):
    def get(self, request):
        data = {'uuid': uuid.uuid4()}
        return Response(data)


class AddToCartView(CreateAPIView):
    serializer_class = ShoppingCartSerializer


class ShoppingCartView(ListAPIView):
    serializer_class = ShoppingCartSerializer

    def get_queryset(self):
        cart_id = self.kwargs.get('cart_id')
        return get_list_or_404(ShoppingCart, cart_id=cart_id)


class UpdateCartItemView(UpdateAPIView):
    serializer_class = UpdateCartSerializer

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(ShoppingCart, id=id)


class DeleteCartView(APIView):
    def delete(self, request, *args, **kwargs):
        cart_id = kwargs.get('cart_id')
        ShoppingCart.objects.filter(cart_id=cart_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RemoveItemView(APIView):
    def delete(self, request, *args, **kwargs):
        item_id = kwargs.get('item_id')
        ShoppingCart.objects.filter(id=item_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TotalAmountView(APIView):
    def get(self, request, *args, **kwargs):
        cart_id = kwargs.get('cart_id')
        data = {'total': ShoppingCart.get_total_amount(cart_id=cart_id)}
        return Response(data=data, status=status.HTTP_200_OK)

from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Orders
from .serializers import OrdersSerializer
from utils import get_object_or_404


class CreateOrdersView(CreateAPIView):
    serializer_class = OrdersSerializer


class OrderDetailView(RetrieveAPIView):
    serializer_class = OrdersSerializer

    def get_object(self):
        id = self.kwargs['id']
        return get_object_or_404(Orders, id=id)


class OrderInCustomerView(ListAPIView):
    serializer_class = OrdersSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.orders_set.all()

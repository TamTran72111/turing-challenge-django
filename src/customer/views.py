from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Customer
from .serializers import CustomerSerializer, CustomerRegisterSerializer


class CustomerView(RetrieveUpdateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class CustomerRegisterView(CreateAPIView):
    serializer_class = CustomerRegisterSerializer
    permission_classes = [AllowAny]

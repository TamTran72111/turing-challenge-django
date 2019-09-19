from rest_framework.generics import ListAPIView

from shipping.models import Shipping
from shipping.serializers import ShippingSerializer
from .models import ShippingRegion
from .serializers import ShippingRegionSerializer


class ShippingRegionView(ListAPIView):
    serializer_class = ShippingRegionSerializer
    queryset = ShippingRegion.objects.all()


class ShippingView(ListAPIView):
    serializer_class = ShippingSerializer

    def get_queryset(self):
        region_id = self.kwargs.get('region_id')
        return Shipping.objects.filter(shipping_region__id=region_id)

from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from attributeValue.serializers import AttributeValueSerializer, ProductAttributeSerializer
from productAttribute.models import ProductAttribute
from .models import Attribute
from .serializers import AttributeSerializer


class AttributeViewset(ReadOnlyModelViewSet):
    serializer_class = AttributeSerializer
    queryset = Attribute.objects.all()


class AttributeValueView(ListAPIView):
    serializer_class = AttributeValueSerializer

    def get_queryset(self):
        return Attribute.get_values_from_id(self.kwargs.get('id'))


class ProductAttributeView(ListAPIView):
    serializer_class = ProductAttributeSerializer

    def get_queryset(self):
        return ProductAttribute.get_attribute_values_from_product_id(
            self.kwargs.get('id'))

from rest_framework import serializers

from .models import Shipping


class ShippingSerializer(serializers.ModelSerializer):
    shipping_id = serializers.ReadOnlyField(source='id')
    shipping_region_id = serializers.ReadOnlyField(source='shipping_region.id')

    class Meta:
        model = Shipping
        exclude = ['id', 'shipping_region']

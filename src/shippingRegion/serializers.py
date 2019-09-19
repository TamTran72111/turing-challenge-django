from rest_framework import serializers

from .models import ShippingRegion


class ShippingRegionSerializer(serializers.ModelSerializer):
    shipping_region_id = serializers.ReadOnlyField(source='id')

    class Meta:
        model = ShippingRegion
        exclude = ['id']

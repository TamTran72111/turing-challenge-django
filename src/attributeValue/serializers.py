from rest_framework import serializers

from .models import AttributeValue


class AttributeValueSerializer(serializers.ModelSerializer):
    attribute_value_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = AttributeValue
        fields = ('attribute_value_id', 'value')


class ProductAttributeSerializer(AttributeValueSerializer):
    attribute_name = serializers.CharField(source='attribute.name')
    attribute_value = serializers.CharField(source='value')

    class Meta:
        model = AttributeValue
        fields = ('attribute_name', 'attribute_value_id', 'attribute_value')

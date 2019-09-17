from rest_framework import serializers

from .models import Attribute


class AttributeSerializer(serializers.ModelSerializer):
    attribute_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Attribute
        fields = ('attribute_id', 'name')

from rest_framework import serializers

from .models import Tax


class TaxSerializer(serializers.ModelSerializer):
    tax_id = serializers.ReadOnlyField(source='id')

    class Meta:
        model = Tax
        exclude = ['id']

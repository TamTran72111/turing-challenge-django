from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='customer.username')

    class Meta:
        model = Review
        fields = ('username', 'review', 'rating', 'created_on')
        extra_kwargs = {
            'created_on': {'read_only': True}
        }

    def create(self, validated_data):
        product_id = self.context['view'].kwargs.get('id')
        validated_data['customer'] = self.context['request'].user
        validated_data['product_id'] = product_id
        return super().create(validated_data)

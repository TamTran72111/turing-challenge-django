from rest_framework import serializers

from .models import ShoppingCart


class ShoppingCartSerializer(serializers.ModelSerializer):
    item_id = serializers.ReadOnlyField(source='id')
    product_id = serializers.IntegerField(source='product.id')
    name = serializers.ReadOnlyField(source='product.name')
    price = serializers.ReadOnlyField(source='product.price')
    subtotal = serializers.SerializerMethodField()
    image = serializers.ReadOnlyField(source='product.image')

    class Meta:
        model = ShoppingCart
        fields = ('item_id', 'name', 'attributes', 'product_id',
                  'image', 'price', 'quantity', 'subtotal', 'cart_id')
        extra_kwargs = {'cart_id': {'write_only': True},
                        'quantity': {'read_only': True}}

    def create(self, validated_data):
        return ShoppingCart.add_to_cart(validated_data)

    def get_subtotal(self, obj):
        return obj.quantity * obj.product.price


class UpdateCartSerializer(ShoppingCartSerializer):
    product_id = serializers.ReadOnlyField(source='product.id')

    class Meta:
        model = ShoppingCart
        fields = ('item_id', 'name', 'attributes', 'product_id',
                  'image', 'price', 'quantity', 'subtotal')
        extra_kwargs = {'attributes': {'read_only': True}}

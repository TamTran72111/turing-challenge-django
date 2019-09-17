from rest_framework import serializers

from .models import Product


class SingleProductSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='id')
    image2 = serializers.CharField(source='image_2')

    class Meta:
        model = Product
        fields = ('product_id', 'name', 'description',
                  'price', 'discounted_price', 'image',
                  'image2', 'thumbnail', 'display')


class ProductsSerializer(SingleProductSerializer):
    class Meta:
        model = Product
        fields = ('product_id', 'name', 'description',
                  'price', 'discounted_price', 'thumbnail')

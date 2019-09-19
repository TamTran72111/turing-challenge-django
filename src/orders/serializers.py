from django.http import Http404
from rest_framework import serializers

from shoppingCart.models import ShoppingCart
from .models import Orders
from orderDetail.models import OrderDetail


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    order_id = serializers.ReadOnlyField(source='id')
    cart_id = serializers.CharField(max_length=40, write_only=True)
    shipping_id = serializers.IntegerField(write_only=True)
    tax_id = serializers.IntegerField(write_only=True)
    details = OrderDetailSerializer(
        source='orderdetail_set', many=True, read_only=True)

    class Meta:
        model = Orders
        fields = ('order_id', 'cart_id', 'shipping_id',
                  'created_on', 'shipped_on', 'status',
                  'total_amount', 'comments', 'tax_id', 'details')
        extra_kwargs = {'created_on': {'read_only': True},
                        'shipped_on': {'read_only': True},
                        'status': {'read_only': True},
                        'total_amount': {'read_only': True},
                        'comments': {'read_only': True}, }

    def create(self, validated_data):
        customer = self.context['request'].user
        cart_id = validated_data['cart_id']
        shipping_id = validated_data['shipping_id']
        tax_id = validated_data['tax_id']
        total_amount = ShoppingCart.get_total_amount(cart_id)
        if total_amount == 0:
            raise Http404
        order = Orders.objects.create(total_amount=total_amount,
                                      shipping_id=shipping_id,
                                      tax_id=tax_id,
                                      customer=customer)
        order.add_details(cart_id)
        return order

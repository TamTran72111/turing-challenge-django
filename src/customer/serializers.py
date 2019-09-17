from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    credit_card = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ('username', 'email', 'address_1', 'address_2', 'city', 'region', 'postal_code', 'country', 'shipping_region', 'day_phone', 'eve_phone', 'mob_phone',
                  'credit_card')

    def get_credit_card(self, obj):
        length = len(obj.credit_card)
        if length > 4:
            return 'X' * (length - 4) + obj.credit_card[-4:]
        return obj.credit_card


class CustomerRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Default shipping id to avoid not null field
        validated_data['shipping_region_id'] = 1

        instance = super().create(validated_data)

        instance.set_password(validated_data['password'])
        instance.save()

        return instance

    def to_representation(self, instance):
        """Modify the method to add token"""
        # Call the parent method
        ret = super().to_representation(instance)

        # Add access token and refresh token
        refresh = RefreshToken.for_user(instance)
        token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        ret['token'] = token

        return ret

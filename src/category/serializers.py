from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(source='id', read_only=True)
    department_id = serializers.IntegerField(
        source='department.id', read_only=True)

    class Meta:
        model = Category
        fields = ('category_id', 'name', 'description', 'department_id')

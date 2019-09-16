from rest_framework import serializers

from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    department_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Department
        fields = ('department_id', 'name', 'description')

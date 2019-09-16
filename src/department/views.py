from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView

from .models import Department
from .serializers import DepartmentSerializer


class DepartmentView(RetrieveAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DepartmentListView(ListAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

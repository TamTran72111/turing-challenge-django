from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Department
from .serializers import DepartmentSerializer


class DepartmentViewset(ReadOnlyModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

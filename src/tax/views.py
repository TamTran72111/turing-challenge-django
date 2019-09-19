from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Tax
from .serializers import TaxSerializer


class TaxViewset(ReadOnlyModelViewSet):
    serializer_class = TaxSerializer
    queryset = Tax.objects.all()

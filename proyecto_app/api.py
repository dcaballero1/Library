from rest_framework import viewsets, permissions
from .models import libro
from .serializers import libroSerializers

class libroViewSet(viewsets.ModelViewSet):
    queryset = libro.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = libroSerializers

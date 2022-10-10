from rest_framework import viewsets, permissions
from .models import Libro, Imprenta, Lector, Biblioteca
from .serializers import libroSerializers, imprentaSerializers, lectorSerializer, bibliotecaSerializer


class libroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = libroSerializers

class imprentaViewSet(viewsets.ModelViewSet):
    queryset = Imprenta.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = imprentaSerializers

class lectorViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class = lectorSerializer

class bibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = bibliotecaSerializer
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *

class bookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = bookSerializers

class printingViewSet(viewsets.ModelViewSet):
    queryset = Printing.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = printingSerializers

class readerViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class = readerSerializer

class bookstoreViewSet(viewsets.ModelViewSet):
    queryset = BookStore.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = bookstoreSerializer
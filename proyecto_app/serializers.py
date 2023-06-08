from rest_framework import serializers
from .models import Book, Printing, Reader, BookStore

class bookSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('__all__')
        read_only_fields = ('created_at',)


class printingSerializers(serializers.HyperlinkedModelSerializer):
    books=serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    class Meta:
        model = Printing
        fields = ('__all__')
        read_only_fields = ('created_at',)

class readerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reader
        fields = ('__all__')

class bookstoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=BookStore
        fields=('__all__')
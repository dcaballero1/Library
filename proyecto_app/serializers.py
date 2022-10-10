from rest_framework import serializers
from .models import Libro, Imprenta, Lector, Biblioteca

class libroSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Libro
        fields = ('title','resume', 'author', 'created_at', 'copia','id_imprenta')
        read_only_fields = ('created_at',)


class imprentaSerializers(serializers.HyperlinkedModelSerializer):
    libros=serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    class Meta:
        model = Imprenta
        fields = ('libros', 'nombre')
        read_only_fields = ('created_at',)

class lectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lector
        fields = ('nombre','libro_ocupado')

class bibliotecaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Biblioteca
        fields=('nombre', 'libros')
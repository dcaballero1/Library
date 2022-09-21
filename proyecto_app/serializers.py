from rest_framework import serializers
from .models import libro

class libroSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = libro
        fields = ('__all__')
        read_only_fields = ('created',)
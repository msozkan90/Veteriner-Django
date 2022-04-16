from hayvanlar.models import AnimalOwners,Animals
from rest_framework import serializers



class AnimalOwnersSerializers(serializers.ModelSerializer):
    class Meta:
        model=AnimalOwners
        fields='__all__'
        read_only_fields = ['id']

class AnimalsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Animals
        fields='__all__'
        read_only_fields = ['id']


from rest_framework import generics
from hayvanlar.api.serializers import AnimalsSerializers,AnimalOwnersSerializers
from hayvanlar.models import AnimalOwners,Animals
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminUserOrReadOnly
from .pagination import StandardResultsSetPagination
class AnimalsListCreateAPIView(generics.ListCreateAPIView):
    queryset=Animals.objects.all()
    serializer_class=AnimalsSerializers
    permission_classes=[IsAuthenticated]
    pagination_class= StandardResultsSetPagination

class OwnersListCreateAPIView(generics.ListCreateAPIView):
    queryset=AnimalOwners.objects.all()
    serializer_class=AnimalOwnersSerializers
    permission_classes=[IsAuthenticated]
    pagination_class= StandardResultsSetPagination


class AnimalsDetailCreateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Animals.objects.all()
    serializer_class=AnimalsSerializers
    permission_classes=[IsAdminUserOrReadOnly,IsAuthenticated]


class OwnersDetailCreateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=AnimalOwners.objects.all()
    serializer_class=AnimalOwnersSerializers
    permission_classes=[IsAdminUserOrReadOnly,IsAuthenticated]

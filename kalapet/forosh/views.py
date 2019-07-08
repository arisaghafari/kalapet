from .serializers import *
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class AdvertismentList(generics.ListCreateAPIView):
    queryset = Advertisment.objects.all()
    serializer_class = AdvertismentSerializer


class AdvertismentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advertisment.objects.all()
    serializer_class = AdvertismentSerializer

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category',)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class VetList(generics.ListCreateAPIView):
    queryset = Vet.objects.all()
    serializer_class = VetSerializer


class VetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vet.objects.all()
    serializer_class = VetSerializer

from django.shortcuts import render
from .models import *
# from  pip import __main__
from .serializers import *
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

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
    filterset_fields = ('category')

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
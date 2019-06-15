from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics

class AdvertismentList(generics.ListCreateAPIView):
    queryset = Advertisment.objects.all()
    serializer_class = AdvertismentSerializer


class AdvertismentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advertisment.objects.all()
    serializer_class = AdvertismentSerializer



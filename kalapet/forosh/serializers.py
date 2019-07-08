from rest_framework import serializers
from .models import *

class AdvertismentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisment
        fields = ('title', 'description', 'image')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'category', 'cost', 'description', 'supplier', 'expiration', 'image')

class VetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vet
        fields = ('username', 'description')
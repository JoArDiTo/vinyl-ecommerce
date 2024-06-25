from rest_framework import serializers
from .models import *

class VinylSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vinyl
        fields = '__all__'
        
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class VinylCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VinylCategory
        fields = '__all__'
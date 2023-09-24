from rest_framework import serializers
from .models import ImagePrediction

class ImagePredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePrediction
        fields = '__all__'

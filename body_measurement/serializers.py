from rest_framework import serializers
from .models import ImagePrediction


class ImagePredictionSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)

    class Meta:
        model = ImagePrediction
        fields = "__all__"

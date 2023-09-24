from rest_framework import generics, status
from rest_framework.response import Response
from .models import ImagePrediction
from .serializers import ImagePredictionSerializer
from roboflow import Roboflow
from decouple import config


def body_measurement(image):
    rf = Roboflow(api_key=config("API_KEY"))
    project = rf.workspace().project("body-measurement-zmbgv")
    model = project.version(1).model
    prediction = model.predict(
        image,
        confidence=40,
        overlap=30,
    ).json()
    return prediction


class ImagePredictionView(generics.CreateAPIView):
    queryset = ImagePrediction.objects.all()
    serializer_class = ImagePredictionSerializer

    def create(self, request, *args, **kwargs):
        image = request.data.get("image")

        predictions = body_measurement(image)

        image_prediction = ImagePrediction(image=image, predictions=predictions)
        image_prediction.save()

        serializer = ImagePredictionSerializer(image_prediction)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

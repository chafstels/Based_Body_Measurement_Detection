from rest_framework import generics, status
from rest_framework.response import Response
from .models import ImagePrediction
from .serializers import ImagePredictionSerializer
from roboflow import Roboflow
from decouple import config
import tempfile


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
        image_file = request.data.get("image")

        if image_file:
            with tempfile.NamedTemporaryFile(delete=True) as temp_file:
                temp_file.write(image_file.read())
                temp_file.flush()
                temp_file_path = temp_file.name

                predictions = body_measurement(temp_file_path)

                image_prediction = ImagePrediction(
                    image=image_file, predictions=predictions
                )
                image_prediction.save()

                serializer = ImagePredictionSerializer(image_prediction)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"message": "The image file has not been transferred."},
                status=status.HTTP_400_BAD_REQUEST,
            )

from django.urls import path
from .views import ImagePredictionView

urlpatterns = [
    path(
        "api/create-prediction/",
        ImagePredictionView.as_view(),
        name="create-prediction",
    ),
]

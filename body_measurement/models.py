from django.db import models

class ImagePrediction(models.Model):
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    predictions = models.JSONField()
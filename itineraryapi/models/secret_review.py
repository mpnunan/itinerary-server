from django.db import models
from .trip import Trip
from .activity import Activity

class SecretReview(models.Model):

    trip = models.ForeignKey(Trip, null=True, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, null=True, on_delete=models.CASCADE)
    review = models.CharField(max_length=150)

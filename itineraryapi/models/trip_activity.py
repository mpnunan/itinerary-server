from django.db import models
from .activity import Activity
from .trip import Trip


class TripActivity(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

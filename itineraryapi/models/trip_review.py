from django.db import models
from .activity import Activity
from .trip import Trip
from .admin import Admin


class TripReview(models.Model):
    user = models.ForeignKey(Admin, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='trip_reviews')
    review = models.CharField(max_length=150)

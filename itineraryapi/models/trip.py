from django.db import models
from .traveler import Traveler
from .admin import Admin


class Trip(models.Model):

    destination = models.CharField(max_length=50)
    transportation = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(Admin, on_delete=models.CASCADE, default=1)

    def activities(self):
        return [activity_trip.activity for activity_trip in self.activity_trips.all()]

from django.db import models
from .traveler import Traveler
# from .destination import Destination


class Trip(models.Model):

    destination = models.CharField(max_length=50)
    transportation = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE)

    def activities(self):
        return [activity_trip.activity for activity_trip in self.activity_trips.all()]

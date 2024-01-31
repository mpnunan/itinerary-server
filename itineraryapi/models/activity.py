from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=50)
    length_of_time = models.CharField(max_length=25)
    cost = models.IntegerField()

    @property
    def planned(self):
        return self.__planned
    
    @planned.setter
    def planned(self, value):
        self.__planned = value

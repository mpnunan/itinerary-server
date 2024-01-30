from django.db import models


class Activity(models.Model):
    name = models.CharField()
    description = models.TextField(max_length=50)
    length_of_time = models.CharField()
    cost = models.IntegerField()

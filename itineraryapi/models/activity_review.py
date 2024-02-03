from django.db import models
from .admin import Admin
from .activity import Activity


class ActivityReview(models.Model):
    user = models.ForeignKey(
        Admin, on_delete=models.CASCADE, related_name='activity_reviews')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    review = models.TextField(max_length=150)

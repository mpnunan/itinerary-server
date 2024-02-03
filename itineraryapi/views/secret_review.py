from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from itineraryapi.models import SecretReview, Trip, Activity


class SecretReviewView(ViewSet):
    
    def list(self, request):
        secret_reviews = SecretReview.objects.all()
        serializer = SecretReviewSerializer(secret_reviews, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        trip = Trip.objects.get(pk=request.data["trip"])
        activity = Activity.objects.get(pk=request.data["activity"])
        secret_review = SecretReview.objects.create(
            trip=trip,
            actrivity=activity,
            review=request.data["review"]
        )
        serializer = SecretReviewSerializer(secret_review)
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        secret_review = SecretReview.objects.get(pk=pk)
        secret_review.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class SecretReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecretReview
        fields = ('id', 'trip', 'activity', 'review')
        depth = 1

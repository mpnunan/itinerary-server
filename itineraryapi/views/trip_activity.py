from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from itineraryapi.models import TripActivity, Trip, Activity


class TripActivityView(ViewSet):
    """Itinerary Trip Activity Link"""

    def retrieve(self, request, pk):
        """Handle GET requests for trip activity"""
        try:
            tripactivity = TripActivity.objects.get(pk=pk)
            serializer = TripActivitySerializer(tripactivity)
            return Response(serializer.data)
        except TripActivity.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get ALL trip activities"""
        tripactivity = TripActivity.objects.all()
        serializer = TripActivitySerializer(tripactivity, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk):
        """Handle DELETE request for trip activity"""
        tripactivity = TripActivity.objects.get(pk=pk)
        tripactivity.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        """Handle POST for trip activity"""
        trip = Trip.objects.get(pk=request.data["trip"])
        activity = Activity.objects.get(pk=request.data["activity"])
        tripactivity = TripActivity.objects.create(
            trip=trip,
            activity=activity
        )
        serializer = TripActivitySerializer(tripactivity)
        return Response(serializer.data)


class TripActivitySerializer(serializers.ModelSerializer):
    """JSON Serializer for trips and activity"""
    class Meta:
        model = TripActivity
        fields = ('id', 'trip', 'activity')
        depth = 1

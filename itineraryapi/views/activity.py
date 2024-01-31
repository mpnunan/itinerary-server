"""View module for handling requests about Activities"""
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from itineraryapi.models import Activity, TripActivity


class ActivityView(ViewSet):
    """Itinerary View"""

    def retrieve(self, request, pk):
        """Hnadle GET requests for activities"""
        try:
            activitys = Activity.objects.get(pk=pk)
            serializer = ActivitySerializer(activitys)
            return Response(serializer.data)
        except Activity.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get ALL Activities"""
        activitys = Activity.objects.all()
        
        trip = request.query_params.get('trip')
        for activity in activitys:
            activity.planned = len(TripActivity.objects.filter(
                trip_id=trip, activity_id=activity
            )) > 0
        
        serializer = ActivitySerializer(activitys, many=True)
        return Response(serializer.data)

    def create(self, request):
        activitys = Activity.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            length_of_time=request.data["length_of_time"],
            cost=request.data["cost"]
        )
        serializer = ActivitySerializer(activitys)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for updating Activities"""
        activitys = Activity.objects.get(pk=pk)
        activitys.name = request.data.get("name")
        activitys.description = request.data.get("description")
        activitys.length_of_time = request.data.get("length_of_time")
        activitys.cost = request.data.get("cost")
        activitys.save()
        return Response({'message': 'Activity updated successfully'}, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        """Handle DELETE requests for Activities"""
        activitys = Activity.objects.get(pk=pk)
        activitys.delete()
        return Response({'message': 'Activity deleted'}, status=status.HTTP_204_NO_CONTENT)


class ActivitySerializer(serializers.ModelSerializer):
    """JSON Serializer for acitivity"""
    class Meta:
        model = Activity
        fields = ('id', 'name', 'description', 'length_of_time', 'cost', 'planned')

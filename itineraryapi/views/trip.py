from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from itineraryapi.models import Trip, Traveler


class TripView(ViewSet):

    def retrieve(self, request, pk):
        try:
            trip = Trip.objects.get(pk=pk)
            serializer = TripSerializer(trip)
            return Response(serializer.data)
        except Trip.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        trips = Trip.objects.all()
        serializer = TripSerializerShallow(trips, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        traveler=Traveler.objects.get(pk=request.data["travelerId"])
        trip = Trip.objects.create(
            destination=request.data["destination"],
            transportation=request.data["transportation"],
            start_date=request.data["startDate"],
            end_date=request.data["endDate"],
            traveler=traveler
        )
        serializer = TripSerializerShallow(trip)
        return Response(serializer.data)
    
    def update(self, request, pk):
        traveler=Traveler.objects.get(pk=request.data["travelerId"])
        trip = Trip.objects.get(pk=pk)
        trip.destination=request.data["destination"]
        trip.transportation=request.data["transportation"]
        trip.start_date=request.data["startDate"]
        trip.end_date=request.data["endDate"]
        trip.traveler=traveler
        trip.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        trip = Trip.objects.get(pk=pk)
        trip.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traveler
        fields = ('id', 'destination', 'transportation', 'start_date', 'end_date', 'traveler')
        depth = 1
        
class TripSerializerShallow(serializers.ModelSerializer):
    class Meta:
        model = Traveler
        fields = ('id', 'destination', 'transportation', 'start_date', 'end_date', 'traveler_id')

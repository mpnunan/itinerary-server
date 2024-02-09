from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from itineraryapi.models import Trip, Traveler, Activity, TripActivity, TripReview, Admin
from rest_framework.decorators import action


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
        user=Admin.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        trip = Trip.objects.create(
            destination=request.data["destination"],
            transportation=request.data["transportation"],
            start_date=request.data["startDate"],
            end_date=request.data["endDate"],
            user=user
        )
        serializer = TripSerializerShallow(trip)
        return Response(serializer.data)
    
    def update(self, request, pk):
        user=Admin.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        trip = Trip.objects.get(pk=pk)
        trip.destination=request.data["destination"]
        trip.transportation=request.data["transportation"]
        trip.start_date=request.data["startDate"]
        trip.end_date=request.data["endDate"]
        trip.user=user
        trip.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        trip = Trip.objects.get(pk=pk)
        trip.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['post'], detail=True)
    def add_activity(self, request, pk):

        trip = Trip.objects.get(pk=pk)
        activity=Activity.objects.get(pk=request.data["activityId"])
        trip_activity =  TripActivity.objects.create(
            trip=trip,
            activity=activity,
        )
        return Response({'message': 'Item added'}, status=status.HTTP_201_CREATED)

    @action(methods=['put'], detail=True)
    def remove_activity(self, request, pk):

        trip = Trip.objects.get(pk=pk)
        activity=Activity.objects.get(pk=request.data["activityId"])
        trip_activities = TripActivity.objects.filter(
            trip=trip,
            activity=activity
        )
        if len(trip_activities) > 0:
            trip_activities[0].delete()
        else:
            pass
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['post'], detail=True)
    def leave_review(self, request, pk):

        trip = Trip.objects.get(pk=pk)
        user = Admin.objects.get(uid=request.data["user"])
        review = request.data["review"]
        trip_review =  TripReview.objects.create(
            trip=trip,
            user=user,
            review=review
        )
        return Response({'message': 'Item added'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['put'], detail=True)
    def delete_review(self, request, pk):

        trip = Trip.objects.get(pk=pk)
        user=Admin.objects.get(uid=request.data["user"])
        review = request.data["review"]
        trip_reviews = TripReview.objects.filter(
            trip=trip,
            user=user,
            review=review
        )
        trip_reviews.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class TripActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'name', 'description', 'length_of_time', 'cost')

class TripSerializer(serializers.ModelSerializer):
    activities = TripActivitySerializer(many=True, read_only=True)
    reviews = serializers.SerializerMethodField()
    def get_reviews(self, obj):
        return [{trip_review.review, trip_review.user.name} for trip_review in TripReview.objects.filter(trip=obj)]
    class Meta:
        model = Trip
        fields = ('id', 'destination', 'transportation', 'start_date', 'end_date', 'user', 'activities', 'reviews')
        depth = 1
        
class TripSerializerShallow(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'destination', 'transportation', 'start_date', 'end_date', 'user_id')

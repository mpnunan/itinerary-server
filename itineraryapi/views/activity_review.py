from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from itineraryapi.models import ActivityReview, Activity, Admin


class ActivityReviewView(ViewSet):
    """Itierary Activity Review View"""

    def retrieve(self, request, pk):
        """Handle GET requests for activity reviews"""
        try:
            activityreview = ActivityReview.objects.get(pk=pk)
            serializer = ActivityReviewSerializer(activityreview)
            return Response(serializer.data)
        except ActivityReview.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get ALL activity reviews"""
        activityreview = ActivityReview.objects.all()

        activity = request.query_params.get('activity', None)

        if activity is not None:
            activityreview = activityreview.filter(activity_id=activity)

        serializer = ActivityReviewSerializer(activityreview, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST for activity review"""
        user = Admin.objects.get(uid=request.data["user"])
        activity = Activity.objects.get(pk=request.data["activity"])
        activityreview = ActivityReview.objects.create(
            activity=activity,
            user=user,
            review=request.data["review"]
        )
        serializer = ActivityReviewSerializer(activityreview)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        """Handle DELETE requests for activity reviews"""
        acitivtyreview = ActivityReview.objects.get(pk=pk)
        acitivtyreview.delete()
        return Response({'message': 'Review deleted'}, status=status.HTTP_204_NO_CONTENT)


class ActivityReviewSerializer(serializers.ModelSerializer):
    """JSON Serilaizer for activity reviews"""
    class Meta:
        model = ActivityReview
        fields = ('id', 'user', 'activity', 'review')

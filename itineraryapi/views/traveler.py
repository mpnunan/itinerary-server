from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from itineraryapi.models import Traveler


class TravelerView(ViewSet):

    def retrieve(self, request, pk):
        try:
            traveler = Traveler.objects.get(pk=pk)
            serializer = TravelerSerializer(traveler)
            return Response(serializer.data)
        except Traveler.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        travelers = Traveler.objects.all()
        serializer = TravelerSerializer(travelers, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        traveler = Traveler.objects.create(
            name=request.data["name"],
            email=request.data["email"],
            phone=request.data["phone"]
        )
        serializer = TravelerSerializer(traveler)
        return Response(serializer.data)
    
    def update(self, request, pk):
        traveler = Traveler.objects.get(pk=pk)
        traveler.name=request.data["name"]
        traveler.email=request.data["email"]
        traveler.phone=request.data["phone"]
        traveler.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        traveler = Traveler.objects.get(pk=pk)
        traveler.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class TravelerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traveler
        fields = ('id', 'name', 'email', 'phone')

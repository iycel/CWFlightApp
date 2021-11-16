from django.shortcuts import render
from django.http import HttpResponse
# from flight.forms import FlightReservationForm, Flight
from flight.models import Flight
from flight.serializers import FlightReservationSerializer, Flight, FlightSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def home(request):
    return HttpResponse('<h1>Hi</h1>')
    
@api_view(['GET', 'POST'])
def flights(request):
    if request.method == 'GET':
        querset = Flight.objects.all()
        serializer = FlightSerializer(querset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def flightsDetails(request, pk): 
    querset = Flight.objects.get(id=pk)
    if request.method == 'GET':
        serializer = FlightSerializer(querset)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FlightSerializer(instance=querset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # serializer._data['success'] = 'Todo succesfully updated ...'
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        querset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from django.shortcuts import render
from django.http import HttpResponse
# from flight.forms import FlightReservationForm, Flight
from flight.models import Flight
from flight.serializers import FlightReservationSerializer, Flight, FlightSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


def home(request):
    return HttpResponse('<h1>Hi</h1>')
    
@api_view(['GET'])
def flightlist(request):
    querset = Flight.objects.all()
    serializer = FlightSerializer(querset, many=True)
    return Response(serializer.data)




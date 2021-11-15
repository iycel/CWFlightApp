from rest_framework import serializers
from .models import Flight, FlightReservation

class FlightReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightReservation
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['flight_number', 'operating_airlines', 'date_of_departure']
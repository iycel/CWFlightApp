from rest_framework import serializers
from .models import Flight, FlightReservation, OperatingAirlines

class FlightReservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FlightReservation
        fields = '__all__'

class FlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flight
        fields = ['flight_number', 'operating_airlines', 'date_of_departure']
        lookup_field = 'operating_airlines'

class OperatingAirlinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatingAirlines
        fields = '__all__'
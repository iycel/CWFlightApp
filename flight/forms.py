from django import forms
from flight.models import Flight, FlightReservation

class FlightReservationForm(forms.ModelForm):
    class Meta:
        model = FlightReservation
        fields = '__all__'
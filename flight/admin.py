from django.contrib import admin
from .models import Flight, FlightReservation, OperatingAirlines, Passenger

class FlightAdmin(admin.ModelAdmin):
    list_display = [
        'flight_number',
        'operating_airlines',
        'departure_city',
        'arrival_city',
        'date_of_departure',
    ]

admin.site.register(Flight, FlightAdmin)
admin.site.register(FlightReservation)
admin.site.register(Passenger)
admin.site.register(OperatingAirlines)


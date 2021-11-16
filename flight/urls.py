from django.urls import path
# from flight.views import home, flightlist, flightCreate, flightUpdate
from flight.views import home, flights, flightsDetails


app_name = 'flight'
urlpatterns = [
    path('', home, name='home'),
    # path('flightlist/', flightlist),
    # path('flightcreate/', flightCreate),
    path('flights/', flights, name='flights'),
    # path('flightsupdate/<int:pk>', flightUpdate),
    path('flightdetails/<int:pk>', flightsDetails, name='flightDetails'),
]

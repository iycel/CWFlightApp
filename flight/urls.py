from django.urls import path
from flight.views import home, flightlist


app_name = 'flight'
urlpatterns = [
    path('', home, name='home'),
    path('flightlist/', flightlist)
]

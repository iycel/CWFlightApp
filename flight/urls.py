from django.urls import path
from flight.views import home


app_name = 'flight'
urlpatterns = [
    path('', home, name='home'),
]

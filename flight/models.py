from django.db import models
from django.contrib.auth.models import User

# def user_directory_path(instance, filename):
#     return 'flight/{0}/{1}'.format(instance.author.id, filename)

# class City(models.Model):
#     CITY = {
#         ('06', 'Ankara'),
#         ('34', 'Istanbul'),
#         ('07', 'Antalya'),
#         ('61', 'Trabzon'),
#         ('35', 'Izmir'),
#         ('001', 'Berlin'),
#         ('002', 'London'),
#         ('003', 'New York'),
#         ('004', 'Tokyo'),
#         ('005', 'Sidney'),
#     }

#     arrival_city = models.CharField(choices=CITY, max_length=50)
#     departure_city = models.CharField(choices=CITY, max_length=50)

#     def __str__(self):
#         return self.arrival_city + ' ' + self.departure_city

class OperatingAirlines(models.Model):
    AIRLINES = {
        ('901' , 'Onur Air'),
        ('902' , 'Anadolu Jet'),
        ('903' , 'Turkish Airlines'),
        ('904' , 'Pegasus'),
        ('905' , 'Atlasglobal'),
    }

    name = models.CharField(choices=AIRLINES, max_length=50)

    def __str__(self):
        return f'{self.name}' 

    class Meta:
        ordering = ['name']
class Flight(models.Model):
    flight_number = models.CharField(max_length=15)
    operating_airlines = models.ForeignKey(OperatingAirlines, on_delete=models.CASCADE)  # Hava yolu şirketini silersek uçuşuda siler
    CITY = {
        ('06', 'Ankara'),
        ('34', 'Istanbul'),
        ('07', 'Antalya'),
        ('61', 'Trabzon'),
        ('35', 'Izmir'),
        ('001', 'Berlin'),
        ('002', 'London'),
        ('003', 'New York'),
        ('004', 'Tokyo'),
        ('005', 'Sidney'),
    }

    departure_city = models.CharField(choices=CITY, max_length=50)
    arrival_city = models.CharField(choices=CITY, max_length=50)
    date_of_departure = models.DateTimeField(auto_now=False)

    class Meta :
        ordering = ['-date_of_departure']

    def __str__(self):
        return f'({self.flight_number} | {self.departure_city} - {self.arrival_city} --- {self.date_of_departure})'
    
class Passenger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)
    # flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        ordering = ['last_name']
class FlightReservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE) 
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    first_name = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.flight} {self.passenger}'




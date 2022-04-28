from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return f'(self.name)'


    class Meta :
        verbose_name = 'Country'
        verbose_name_plural= 'Countries'


class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return f'(self.name)'


    class Meta :
        verbose_name = 'City'
        verbose_name_plural= 'Cites'




class Airport(models.Model):
    code = models.CharField(max_length=5)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Flight(models.Model):
    origin = models.ForeignKey(Airport, related_name='origin_flight', on_delete=models.CASCADE)
    destination = models.ForeignKey(Airport, related_name='destination_flight', on_delete=models.CASCADE)
    duration = models.IntegerField()
    date = models.DateTimeField()
    price = models.DecimalField(max_length=12, max_digits=12, decimal_places=2)


class Booking(models.Model):
    customer = models.CharField(max_length=255)
    seat = models.IntegerField()
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

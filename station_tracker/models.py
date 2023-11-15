from django.db import models

# Create your models here.



class Gas_Station(models.Model):
  station_name = models.CharField(max_length=200)
  latitude = models.FloatField()
  longitude = models.FloatField()

  def __str__(self):
    return self.station_name
  
class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    comments = models.TextField()
    gasStationAddr = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
#Note: PhoneNumberField is a custom module for Django installed via pip

class Feedback(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField()
  phone = PhoneNumberField(null=False, blank=False, unique=True)
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  #todo: implement pointer to company
  
  def __str__(self):
    return self.name

class Gas_Station(models.Model):
  station_name = models.CharField(max_length=200)
  latitude = models.FloatField()
  longitude = models.FloatField()

  def __str__(self):
    return self.station_name
  


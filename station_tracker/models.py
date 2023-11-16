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

# Create your models here.
class GasStation(models.Model):
  name = models.CharField(max_length=50)
  regular_gas_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
  premium_gas_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
  diesel_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
  
  def __str__(self):
    return self.name


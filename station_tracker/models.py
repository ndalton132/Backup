from django.db import models

# Create your models here.
class GasStation(models.Model):
  name = models.CharField(max_length=50)
  regular_gas_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
  premium_gas_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
  diesel_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
  
  def __str__(self):
    return self.name
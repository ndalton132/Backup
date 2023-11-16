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

  # Model for the About Us page
class AboutUs(models.Model):
    # Fields for the About Us page
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='about_us_images/')
    # Add any other fields you need for the About Us page

  
def __str__(self):
    return self.name


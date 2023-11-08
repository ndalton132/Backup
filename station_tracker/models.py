from django.db import models

# Create your models here.
class Feedback(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField()
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  #todo: implement pointer to company
  
  def __str__(self):
    return self.name


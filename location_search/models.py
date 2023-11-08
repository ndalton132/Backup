from django.db import models



class Search(models.Model):
    location = models.CharField(max_length = 100)
    range = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.location}"


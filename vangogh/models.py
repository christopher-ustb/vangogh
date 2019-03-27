from django.db import models

# Create your models here.


class Photo(models.Model):
    path = models.CharField(max_length=256)

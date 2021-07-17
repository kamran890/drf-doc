from django.db import models

# Create your models here.

class Car(models.Model):
    """
    This model is intended for Car Object. Any description related to
    model can be added here
    """
    number = models.CharField(max_length=20)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    price = models.CharField(max_length=20)

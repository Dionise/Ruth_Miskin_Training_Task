from statistics import mode
from turtle import title
from xml.parsers.expat import model
from django.db import models
from django.utils.translation import gettext as _
class Registration(models.Model):
    EstablishmentName = models.CharField(  max_length=255)
    EstablishmentStatus = models.CharField(  max_length=10)
    OpenDate = models.DateField()
    CloseDate = models.DateField()
    Town = models.CharField( max_length=64, default="London")
    Postcode =models.CharField( max_length=5, default=None )
    SchoolWebsite = models.CharField(  max_length=255, default=None)
    TelephoneNum = models.CharField( max_length=15, default=None )

    
    
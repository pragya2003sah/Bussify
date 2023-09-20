from django.db import models

# Create your models here.
class app1(models.Model):
    route = models.CharField(("route"),max_length=255)
    latitude = models.FloatField(("latitude"))
    longitude = models.FloatField(("longitude"))
    combined = models.CharField("combined",max_length=255)
    distance = models.IntegerField("diatance")
    departure =models.IntegerField("diatance")
    bustroute =models.IntegerField("diatance")
    arrivaltime = models.TimeField("arrivaltime")
    
    
    
    
from django.db import models

# Create your models here.
class app1(models.Model):
    route = models.CharField(("route"),max_length=255)
    latitude = models.CharField(("latitude"),max_length=255)
    longitude = models.CharField(("longitude"),max_length=255)
    combined = models.CharField("combined",max_length=255)
    distance = models.CharField("distance",max_length=255)
    bustroute =models.CharField("busroute",max_length=255)
    arrivaltime = models.TimeField("arrivaltime")
    def __str__(self):
        return self.route
    
    
    
    
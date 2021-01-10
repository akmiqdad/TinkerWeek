from django.db import models

# Create your models here.
class Event(models.Model):
    event_name=models.CharField(max_length=50, blank=False)
    event_description = models.CharField(max_length=250)
    event_venue=models.CharField(max_length=50, blank=False)
    regn_fees = models.FloatField(blank=False) 
    event_contact = models.CharField(max_length=15)

    def __str__(self):
        return self.event_name

class Participent(models.Model):
    name = models.CharField(max_length=30, blank=False)
    year=models.IntegerField()
    institute_name = models.CharField(max_length=50)
    email = models.EmailField(blank = False)
    phone=models.IntegerField()

    event = models.ForeignKey(Event , on_delete = models.CASCADE,default="")
     
    def __str__(self):
        return self.name
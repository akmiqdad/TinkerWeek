from django.db import models
import datetime
import django.utils.timezone

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=50,blank=False)
    description=models.CharField(max_length=200, blank=False)
    date_added = models.DateTimeField(default=django.utils.timezone.now)
    is_completed = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return self.title
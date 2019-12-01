import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300,null = True, blank = True)
    location = models.CharField(max_length=200,null = True, blank = True)
    qualification = models.CharField(max_length=300,null = True, blank = True)
    event_date = models.DateField('event date',null = True)
    start_time = models.TimeField('start time',null = True)
    end_time = models.TimeField('end time',null = True)
    max_regis = models.IntegerField('maximum participant', null = True, blank = True)
    user = models.ManyToManyField(User, blank=True)
    
    def __str__(self):
        return self.name
    
    def is_future(self):
        if self.event_date  > timezone.now().date():
            return True
        else:
            return False
        
    def is_soon_event(self):
        """Return True if registered events will begin with in 3 days"""
        if (self.event_date <= timezone.now().date() + datetime.timedelta(days=3)) and self.is_future():
            return True
        else:
            return False

    def day_to_event(self):
        return (self.event_date - timezone.now().date()).days
        

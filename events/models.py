import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300,null = True)
    event_date = models.DateField('event date',null = True)
    start_time = models.TimeField('start time',null = True)
    end_time = models.TimeField('end time',null = True)
    user = models.ManyToManyField(User, blank=True)
    def __str__(self):
        return self.name

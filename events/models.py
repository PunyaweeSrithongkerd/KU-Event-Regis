import datetime

from django.db import models
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    event_date = models.DateField('event date')
    start_time = models.TimeField('start time')
    end_time = models.TimeField('end time')
    def __str__(self):
        return self.name

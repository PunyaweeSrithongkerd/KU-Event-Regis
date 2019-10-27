import datetime

from django.db import models
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Date(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateTimeField('date published')
    def __str__(self):
        return self.date

class Duration(models.Model):
    duration = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self):
        return self.duration

class Description(models.Model):
    description = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self):
        return self.description
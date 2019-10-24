from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Event, Date

class IndexView(generic.ListView):
    model = Event
    template_name = 'events/index.html'


    

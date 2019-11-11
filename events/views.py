from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone

from .models import Event

class IndexView(generic.ListView):
    model = Event
    context_object_name = 'events_list'
    template_name = 'events/index.html'
	
    def get_queryset(self):
        """
        Return all upcoming events in the future .
        """
        return Event.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:10]

class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'

class RegisterView(generic.ListView):    
    model = Event
    template_name = 'events/regis.html'

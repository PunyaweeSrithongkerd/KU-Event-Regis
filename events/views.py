from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Event
from django.contrib.auth.models import User

class IndexView(generic.ListView):
    model = Event
    context_object_name = 'events_list'
    template_name = 'events/index.html'
	
    def get_queryset(self):
        """
        Return all upcoming events in the future .
        """
        return Event.objects.filter(event_date__gte=timezone.now()).order_by('event_date')[:10]

class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'

class RegisterView(generic.ListView):    
    model = Event
    template_name = 'events/regis.html'

def regis(request, pk):
    userID = request.POST.get('UserID',False)
    user = User.objects.get(id=userID)

    regis_event = Event.objects.get(pk=pk)

    regis_event.user.add(user)
    regis_event.save()

    return redirect(reverse("events:register"))

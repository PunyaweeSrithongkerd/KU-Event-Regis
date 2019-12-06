from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template.response import TemplateResponse

from .models import Event
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count

import logging

def configure():
    """Configure loggers and log handlers"""
    # write all messages to a file.
    # For a real app, use a configurable absolute path to log file.
    filehandler = logging.FileHandler("log.log")
    filehandler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
             '%(asctime)s %(name)s %(levelname)s: %(message)s' )
    filehandler.setFormatter(formatter)
    # add handler to root logger
    root = logging.getLogger()
    root.setLevel( logging.NOTSET )
    root.addHandler(filehandler)
    # Define a console handler for messages of level WARNING or higher
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    formatter = logging.Formatter(fmt="%(levelname)-8s %(name)s: %(message)s")
    console_handler.setFormatter(formatter)
    root.addHandler( console_handler )
    
class IndexView(generic.ListView):
    model = Event
    context_object_name = 'events_list'
    template_name = 'events/index.html'
	
    def get_queryset(self):
        """
        Return all upcoming events in the future .
        """
        return Event.objects.filter(event_date__gte=timezone.now()).order_by('event_date')[:10]

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['most_popular_event'] = Event.objects.annotate(user_count=Count("user")).order_by("-user_count")[:1]
        return context

class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'

class RegisterView(generic.ListView):    
    model = Event
    template_name = 'events/regis.html'


@login_required(login_url='/accounts/login/') 
def regis(request, pk):
    userID = request.POST.get('UserID',False)
    regis_event = Event.objects.get(pk=pk)
    try:
        user = User.objects.get(id=userID)
    except (KeyError, User.DoesNotExist):
        return redirect(reverse("events:details", args=(regis_event.id,)))
    else:
        regis_event.user.add(user)
        regis_event.save()
        
        configure()
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        print("Logging to ", logger)
        logger.info(f"UserID: {user.id} register event")
        #log_test(logger)

    return redirect(reverse("events:register"))

def unregis(request, pk):
    userID = request.POST.get('UserID',False)

    user = User.objects.get(id=userID)
    regis_event = Event.objects.get(pk=pk)
    
    regis_event.user.remove(user)
    regis_event.save()

    return redirect(reverse("events:register"))

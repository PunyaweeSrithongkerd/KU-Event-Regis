from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.template.response import TemplateResponse
from .models import Event
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver

import logging

def configure():
    """Configure loggers and log handlers"""
    # write all messages to a file.
    # For a real app, use a configurable absolute path to log file.
    filehandler = logging.FileHandler("log.log")
    filehandler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s %(name)s %(levelname)s: %(message)s')
    filehandler.setFormatter(formatter)
    # add handler to root logger
    root = logging.getLogger()
    root.setLevel(logging.NOTSET)
    root.addHandler(filehandler)
    # Define a console handler for messages of level WARNING or higher
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    formatter = logging.Formatter(fmt="%(levelname)-8s %(name)s: %(message)s")
    console_handler.setFormatter(formatter)
    root.addHandler(console_handler)


class IndexView(generic.ListView):
    model = Event
    context_object_name = 'events_list'
    template_name = 'events/index.html'

    def get_queryset(self):
        """
        Return all upcoming events in the future .
        """
        return Event.objects.filter(event_date__gt=timezone.now()).order_by('event_date')[:10]

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['most_popular_event'] = Event.objects.annotate(
            user_count=Count("user")).filter(event_date__gt=timezone.now()).order_by("-user_count")[:1]
##        context['reminder'] = user.event_set.all().filter(
##            event_date__gte=timezone.now() + datetime.timedelta(days=3)).order_by("day_to_event")
        return context


class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'


class RegisterView(generic.ListView):
    model = Event
    template_name = 'events/regis.html'


@login_required(login_url='/accounts/login/')
def regis(request, pk):
    userID = request.POST.get('UserID', False)
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
        logger.info(f"ID {user.id} {user.username} register {regis_event.name} event")
        # log_test(logger)

    return redirect(reverse("events:register"))


def unregis(request, pk):
    userID = request.POST.get('UserID', False)

    user = User.objects.get(id=userID)
    regis_event = Event.objects.get(pk=pk)

    regis_event.user.remove(user)
    regis_event.save()

    configure()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    print("Logging to ", logger)
    logger.info(f"ID {user.id} {user.username} unregister {regis_event.name} event")

    return redirect(reverse("events:register"))


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('events:index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"




@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):    
    configure()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    ip = request.META.get('REMOTE_ADDR')

    logger.info('login user: {user} via ip: {ip}'.format(
        user=user,
        ip=ip
    ))

@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):
    configure()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    ip = request.META.get('REMOTE_ADDR')

    logger.info('logout user: {user} via ip: {ip}'.format(
        user=user,
        ip=ip
    ))

@receiver(user_login_failed)
def user_login_failed_callback(sender, request, credentials, **kwargs):
    configure()
    logger = logging.getLogger()
    logger.setLevel(logging.WARNING)
    ip = request.META.get('REMOTE_ADDR')
    
    logger.warning('login failed for: {credentials} via ip: {ip}'.format(
        credentials=credentials,
        ip=ip
    ))


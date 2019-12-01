import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from events.models import Event


def create_Event(Event_text, days):
    """
    Create a Event with the given `Event_text` and published the
    given number of `days` offset to now.
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Event.objects.create(name=Event_text, event_date=time)


class EventIndexViewTests(TestCase):
    def test_no_Events(self):
        """
        If no Events exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('events:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No events are available.")
        self.assertQuerysetEqual(response.context['events_list'], [])

    def test_past_Event(self):
        """
        Events with a pub_date in the past are displayed on the
        index page.
        """
        create_Event(Event_text="Past Event.", days=-30)
        response = self.client.get(reverse('events:index'))
        self.assertQuerysetEqual(
            response.context['events_list'],
            []
        )

    def test_future_Event(self):
        """
        Events with a pub_date in the future aren't displayed on
        the index page.
        """
        create_Event(Event_text="Future Event.", days=30)
        response = self.client.get(reverse('events:index'))
        self.assertQuerysetEqual(response.context['events_list'], ['<Event: Future Event.>'])

    def test_future_Event_and_past_Event(self):
        """
        Even if both past and future Events exist, only past Events
        are displayed.
        """
        create_Event(Event_text="Past Event.", days=-30)
        create_Event(Event_text="Future Event.", days=30)
        response = self.client.get(reverse('events:index'))
        self.assertQuerysetEqual(
            response.context['events_list'],
            ['<Event: Future Event.>']
        )

    def test_two_past_Events(self):
        """
        The Events index page may display multiple Events.
        """
        create_Event(Event_text="Past Event 1.", days=-30)
        create_Event(Event_text="Past Event 2.", days=-5)
        response = self.client.get(reverse('events:index'))
        self.assertQuerysetEqual(
            response.context['events_list'],
            []
        )


class EventDetailViewTests(TestCase):
    def test_future_Event(self):
        """
        The detail view of a Event with a pub_date in the future
        returns a 404 not found.
        """
        future_Event = create_Event(Event_text='Future Event.', days=5)
        url = reverse('events:details', args=(future_Event.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_past_Event(self):
        """
        The detail view of a Event with a pub_date in the past
        displays the Event's text.
        """
        past_Event = create_Event(Event_text='Past Event.', days=-5)
        url = reverse('events:details', args=(past_Event.id,))
        response = self.client.get(url)
        self.assertContains(response, past_Event.description)

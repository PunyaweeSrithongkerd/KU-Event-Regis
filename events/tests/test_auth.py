import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from events.models import Event
from django.contrib.auth.models import User


def create_event(name, days):
    time = timezone.now() + datetime.timedelta(days=days)
    event = Event.objects.create(name=name, event_date=time)
    return event


class AuthTest(TestCase):
    """Some tests of authentication using django.contrib.auth."""

    def setUp(self):
        self.e1 = create_event("A First Question", days=-1)
        self.username = "testuser"
        self.userpass = "123$*HCfjdksla"
        self.user = User.objects.create_user(self.username, password=self.userpass)

    def test_can_view_event_detail(self):
        """Test that an unauthenticated user can view event detail"""
        url = reverse('events:details', args=[self.e1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/detail.html')

    def test_user_can_login(self):
        """Test that a user can login at the url named 'login'.
           This is the standard name used in django.contrib.auth.urls.
           See: response = self.client.get(reverse('polls:index'))
        """
        login_url = reverse('login')
        response = self.client.post(login_url,
                                    {'username': self.user.username, 'password': self.userpass})
        # This is a weak test: if login succeeds he is redirected.
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('events:index'))
        # Can we use the client session to check valid login?
        # self.client.session

    def test_register_requires_auth_user(self):
        """Test that user must be authenticated to register.
           When authorized user register, he is
           redirected to registered page.
        """
        try:
            self.client.logout(self)
        except Exception:
            pass
        register_url = reverse('events:regis', args=[self.e1.id])
        response = self.client.post(register_url, {'event': self.e1.id})
        self.assertEqual(response.status_code, 302)
        # comparing redirect response to reverse('login') fails
        # because of next=... query param.  Append it.
        expect_url = reverse('login') + '?next=' + register_url
        self.assertRedirects(response, expect_url)

        response = self.client.post(reverse('login'),
                                    {'username': self.user.username, 'password': self.userpass})

        response = self.client.post(register_url, {'event': str(self.e1.id)})
        self.assertEqual(response.status_code, 302)
        expect_url = reverse('events:details', args=(self.e1.id,))
        self.assertRedirects(response, expect_url)
        print("After registered")
        for event in self.user.event_set.all():
            print(event, "regis:", event.regis)

        response = self.client.post(register_url, {'event': '2'})
        self.assertEqual(response.status_code, 302)
        print("After second registered")
        for event in self.user.event_set.all():
            print(event, "regis:", event.regis)

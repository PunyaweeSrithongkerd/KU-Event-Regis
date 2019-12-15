import datetime

from django.test import TestCase
from events.models import Event
from django.utils import timezone


class TestModelEvent(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        Event.objects.create(name = 'Event')
        
    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass
    
    def test_first_name_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
    
    def test_first_name_max_length(self):
        event = Event.objects.get(id=1)
        max_length = event._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_str_(self):
        event = Event.objects.get(id=1)
        name_return = event.name
        self.assertEquals(name_return,'Event')        

    def test_description_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_description_max_length(self):
        event = Event.objects.get(id=1)
        max_length = event._meta.get_field('description').max_length
        self.assertEquals(max_length, 300)       
        
    def test_location_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('location').verbose_name
        self.assertEquals(field_label, 'location')

    def test_location_max_length(self):
        event = Event.objects.get(id=1)
        max_length = event._meta.get_field('location').max_length
        self.assertEquals(max_length, 200)      
        
    def test_qualification_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('qualification').verbose_name
        self.assertEquals(field_label, 'qualification')

    def test_qualification_max_length(self):
        event = Event.objects.get(id=1)
        max_length = event._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)
        
    def test_event_date_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('event_date').verbose_name
        self.assertEquals(field_label, 'event date')
    
    def test_start_time_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('start_time').verbose_name
        self.assertEquals(field_label, 'start time')
        
    def test_end_time_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('end_time').verbose_name
        self.assertEquals(field_label, 'end time')

    def test_max_regis_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('max_regis').verbose_name
        self.assertEquals(field_label, 'maximum participant')

    def test_is_today_or_future(self):
        event = Event.objects.get(id=1)
        event.event_date = timezone.now().date() + datetime.timedelta(days=1)
        self.assertTrue(event.is_today_or_future)

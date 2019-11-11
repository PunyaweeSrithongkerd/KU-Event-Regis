from django.test import TestCase
from events.models import Event
# Create your tests here.
class TestModelEvent(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        Event.objects.create(name = 'Jim brucker')

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
        name_return = event._str_()
        self.assertEquals(name_return,'Jim brucker')
    
     
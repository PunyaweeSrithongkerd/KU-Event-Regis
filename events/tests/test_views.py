from django.test import TestCase
from events.models import Event
# Create your tests here.
class TestIndexView(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        Event.objects.create(name = 'Jim brucker')

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass
    
     
        

    
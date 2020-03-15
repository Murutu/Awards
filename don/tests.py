from django.test import TestCase
from .models import Project

# Create your tests here.

class ProjectTestClass(TestCase):
    def setUp(self):
        self.newuser=User(username='peter')
        self.newuser.save()
        self.projects=Project(title='proj',image='img.jpg',description='fullstackdeveloper',editor=self.newuser)
    


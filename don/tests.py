from django.test import TestCase
from .models import Project

# Create your tests here.

class ProjectTestClass(TestCase):
    def setUp(self):
        self.newuser=User(username='peter')
        self.newuser.save()
        self.projects=Project(title='proj',image='img.jpg',description='fullstackdeveloper',editor=self.newuser)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.projects,Project))
            
    def test_save_project(self):
        self.projects.save_project()
        allprojects=Project.objects.all()
        self.assertTrue(len(allprojects)>0)
        
    def test_delete_projects(self):
        self.projects.save_project()
        self.projects.delete_project()
        allprojects=Project.objects.all()
        self.assertTrue(len(allprojects)==0)
        
    def test_get_projects(self):
        self.projects.save_project()
        firstproject=Project.get_projects()
        self.assertTrue(firstproject is not None)
    


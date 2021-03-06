from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='photos/',null=True)
    bio=models.CharField(max_length=500)
    contact=models.CharField(max_length=30)
    editor=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
        
    @classmethod
    def get_profile(cls):
        profile=cls.objects.all()
        return profile
    
    @classmethod
    def single_profile(cls,user_id):
        profile=cls.objects.filter(editor=user_id)
        return profile
    
    @classmethod
    def get_profilepic_id(cls,imageId):
        profile = cls.objects.filter(id=imageId)
        return imageId
    
    
class Project(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/',blank=True)
    description = HTMLField()
    link = models.URLField(max_length=100,db_index=True,unique=True,blank=True)
    editor=models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def save_project(self):
        self.save()
        
    def delete_project(self):
        self.delete()
        
    @classmethod
    def get_projects(cls):
        project=cls.objects.all()
        return project
    
    @classmethod
    def user_project(cls,project_id):
        project_posted=cls.objects.get(id=project_id)
        return project_posted
    
    @classmethod
    def get_image_id(cls,imageId):
        image_id=cls.objects.filter(id=imageId)
        return image_id
    
class Rating(models.Model):
    editor=models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    design=models.IntegerField()
    usability=models.IntegerField()
    content=models.IntegerField()
    
    def __str__(self):
        return self.design
    
    @classmethod
    def get_rating_byproject_id(cls,project_id):
        rating=cls.objects.filter(project=project_id)
        return rating
    
    
    

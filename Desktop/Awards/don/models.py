from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='photos/',null=True)
    bio = models.CharField(max_length=500)
    contact=models.CharField(max_length=30)
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    
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
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/',blank=True)
    description = HTMLField()
    link = models.URLField(max_length=100,db_index=True,unique=True,blank=True)
    editor=models.ForeignKey(User,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,null=True)
    pub_date=models.DateTimeField(auto_now_add=True)
    
    
    

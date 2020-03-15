from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='photos/',null=True)
    bio = models.CharField(max_length=500)
    contact=models.CharField(max_length=30)
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def save_profile(self):
        self.save()

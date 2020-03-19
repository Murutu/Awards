from rest_framework.serializers import ModelSerializer
from .models import Profile,Project

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio','contact','editor')
        
class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'image', 'description', 'link', 'editor', 'profile', 'pub_date')

from django.conf.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('new/project',views.new_project,name='new-project'),
    path('project/<int:id>/',views.single_project,name='project'),
    path('new/profile',views.new_profile,name='new-profile'),
    path('displayprofile/<int:user_id=current_user.id>/',views.profile,name= 'profile'),
    path('rate',views.add_rating,name='rate'),
    
]


from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('new/project',views.new_project,name='new-project'),
    re_path(r'^project/(\d+)',views.single_projects,name='project'),
    path('new/profile',views.new_profile,name='new-profile'),
    re_path('displayprofile/(\d+)',views.profile,name= 'profile'),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/project/', views.ProjectList.as_view()),
    path('rate',views.add_rating,name='rate'),
    
    
]

if settings.DEBUG:
      urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    


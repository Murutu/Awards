from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .forms import NewProjectForm,NewRatingForm,NewProfileForm
from django.core.exceptions import  ObjectDoesNotExist
from .models import Profile,Project,Rating
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile,Project,Rating
from .serializer import ProfileSerializer,ProjectSerializer


class ProfileList(APIView):
    '''
    Endpoint that returns all profile details. 
    '''
    def get(self,request,format=None):
        all_profile =Profile.objects.all()
        serializers =ProfileSerializer(all_profile,many=True)
        return Response(serializers.data)
    
class ProjectList(APIView):
    '''
    Endpoint that returns all projects posted and their details
    '''
    def get(self,request,format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects,many=True)
        return Response(serializers.data)
    
    
# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    all_projects=Project.objects.all()
    logged_in_user=request.user
    logged_in_user_projects=Project.objects.filter(editor=logged_in_user)
    try:
        profile=Profile.objects.filter(editor=logged_in_user)
    except Profile.DoesNotExist:
        profile=None
    return render(request,'home.html',{"project":logged_in_user_projects,"profile":profile,"allprojects":all_projects})
    
@login_required(login_url='/accounts/login')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project =form.save(commit=False)
            project.editor =current_user
            project.save()
            return redirect('home')
    else:
        form = NewProjectForm()
    return render(request,'new_project.html',{"form":form})
        
@login_required(login_url='/accounts/login')
def single_projects(request,project_id):
    project_posted=Project.objects.get(id=project_id)
    
    return render(request,'project.html',{"project":project_posted})

@login_required(login_url='/accounts/login')
def new_profile(request):
    current_user=request.user
    if request.method =='POST':
        form =NewProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.editor=current_user
            profile.save()
        return redirect('home')
    
    else:
        form= NewProfileForm()
    return render(request,'new_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def profile(request,user_id):
    user= request.user
    current_user = Profile.objects.get(editor=user)
    
    return render(request,'profiledisplay.html', user.username.id)


@login_required(login_url='/accounts/login')
def display_profile(request,user_id):
    try:
        single_profile=Profile.single_profile(user_id)
        projects_posted=Project.user_projects(user_id)
        return render(request,'profiledisplay.html',{"profile":single_profile,"projects":projects_posted})
    except Profile.DoesNotExist:
        messages.info(request,'The user has not set a profile yet')
    except Project.DoesNotExist:
        messages.infor(request,'The user has not posted any project yet')
        return redirect('home')
    
@login_required(login_url='/accounts/login')
def add_rating(request):
    if request.method =='POST':
        design =request.POST.get("design",None)
        usability = request.POST.get("usability",None)
        content=request.POST.get("content",None)
        
    return render(request,'rate.html')




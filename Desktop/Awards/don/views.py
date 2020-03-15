from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Profile,Project,Rating
from django.contrib.auth.models import User

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
        return render('home.html',{"project":logged_in_user_projects,"profile":profile,"allprojects":all_projects})



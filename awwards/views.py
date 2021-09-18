from awwards.models import Profile
from django.shortcuts import render
from awwards.models import Profile, Project
# Create your views here.
def home(request):
    projects = Project.display_projects()
    profile = Profile.objects.all()

    return render(request,'index.html',{"projects":projects,"profile":profile})
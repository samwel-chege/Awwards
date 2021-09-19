
from awwards.models import Profile
from django.shortcuts import render
from awwards.models import Profile, Project
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .serializer import ProjectSerializer,ProfileSerializer
from awwards import serializer
from .forms import ProjectForm
# Create your views here.
def home(request):
    projects = Project.display_projects()
    profile = Profile.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            project.user = request.user
            project.save()
    else:
        form = ProjectForm()
    try:
        project = Project.objects.all()
    except:
        project.DoesNotExist
        project = None

    return render(request,'index.html',{"projects":projects,"profile":profile,"form":form,"project":project})


class ProjectList(APIView):
    def get(self,request,format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects,many=True)
        return Response(serializers.data)

class ProfileList(APIView):
    def get(self,request,format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles,many=True)
        return Response(serializers.data)        






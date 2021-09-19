
from awwards.models import Profile
from django.shortcuts import render
from awwards.models import Profile, Project
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .serializer import ProjectSerializer
from awwards import serializer
# Create your views here.
def home(request):
    projects = Project.display_projects()
    profile = Profile.objects.all()

    return render(request,'index.html',{"projects":projects,"profile":profile})

class ProjectList(APIView):
    def get(self,request,format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects,many=True)
        return Response(serializers.data)



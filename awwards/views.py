
from awwards.models import Profile
from django.shortcuts import render,redirect
from awwards.models import Profile, Project
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .serializer import ProjectSerializer,ProfileSerializer
from awwards import serializer
from .forms import ProjectForm,UploadProjectForm
from django.http.response import Http404, HttpResponseRedirect
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


def uploadproject(request):
    current_user = request.user
    try:
        profile = Profile.objects.get(user = current_user)
    except Profile.DoesNotExist:
        raise Http404()
    if request.method == "POST":
        form = UploadProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = profile
            image.save()
        return redirect('home')
    else:
        form = UploadProjectForm()
    return render(request, 'project/upload_project.html', {"form": form})                







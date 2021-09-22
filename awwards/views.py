
import awwards
from awwards.models import Profile
from django.shortcuts import render,redirect,get_object_or_404
from awwards.models import Profile, Project
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project, Rate
from .serializer import ProjectSerializer,ProfileSerializer
from awwards import serializer
from .forms import ProjectForm,UploadProjectForm,RateForm,ProfileForm
from django.http.response import Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    # projects = Project.display_projects()
    # profile = Profile.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            project.user = request.user
            project.save()
    else:
        form = ProjectForm()
    try:
        project = Project.display_projects()
    except:
        project.DoesNotExist
        project = None

    return render(request,'index.html',{"form":form,"project":project})

@login_required(login_url='/accounts/login/')
def profile(request):
    if request.method=='POST':
        
        form=ProfileForm(request.POST)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=request.user
            profile.save()
    else:
        form=ProfileForm()
    
    try:
        profiles=Profile.objects.all()
    except Profile.DoesNotExist:
        profiles = None

    return render(request, 'profile.html', {'profiles':profiles, 'form':form })
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

def search_projects(request):
    if "project" in request.GET and request.GET["project"]:
        searched_projects = request.GET.get("project")
        projects = Project.search(searched_projects)
        message = f"{searched_projects}"

        return render(request,'search.html',{"message":message,"projects":projects})
    else:
        message = "Try again"
        return render(request,'search.html',{"message":message,}) 


def rate(request, project):
    projects=Project.objects.get(pk=project)
    rate=Rate.objects.filter(project=projects).all()
   
    if request.method=='POST':
        form=RateForm(request.POST)
        if form.is_valid():
            rating=form.save(commit=False)
            rating.user=request.user
            rating.project=projects
            rating.save()

            project_ratings=Rate.objects.filter(project=project)

            design_ratings=[r.design for r in project_ratings]
            design_average=sum(design_ratings) /len(design_ratings)

            content_ratings=[c.content for c in project_ratings]
            content_average=sum(content_ratings) /len(content_ratings)

            usability_ratings=[u.usability for u in project_ratings]
            usability_average=sum(usability_ratings) /len(usability_ratings)

            score=(design_average + content_average + usability_average)/3

            rating.design_average=round(design_average, 2)
            rating.usability_average=round(usability_average, 2)
            rating.content_average=round(content_average, 2)
            rating.score=round(score, 2)
            rating.save()
            
            return HttpResponseRedirect(request.path_info)
    else:
        form=RateForm()
    parameters={
        'project':project,
        'rating_form':form,
        'id':project,
        'rate':rate
     
    }
    return render(request, 'project/rate.html', parameters )

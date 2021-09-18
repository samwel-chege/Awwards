from awwards.models import Project
from rest_framework import viewsets,permissions
from .serializers import ProjectSerializer

#create viewset
class ProjectViewSet(viewsets.ModelViewSet):
    #specify a queryset that is going to take all the model objects
    queryset = Project.objects.all()

    #set permissions
    permission_classes = [
        permissions.AllowAny,
    ]
    #pass the serializer class
    serializer_class = ProjectSerializer

    #return projects of a specific user
    #create a project based on an owner
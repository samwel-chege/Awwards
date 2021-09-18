from rest_framework import serializers
from awwards.models import Profile, Project

#create the project serializer
class ProjectSerializer(serializers.ModelSerializer):
    #create a meta class that will define my model
    class Meta:
        model = Project
        fields = '__all__'

from rest_framework import serializers
from .models import Profile,Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title','image','description','link','profile','create_date')

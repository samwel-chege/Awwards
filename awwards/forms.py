from django import forms
from .models import Project,Profile
from django.forms import ModelForm

class ProjectForm(forms.Form):
    class Meta:
        model = Project
        fields = ('title','image','description','link','profile','create_date')

class ProfileForm(forms.Form):
    class Meta:
        model = Profile
        fields = ('user','photo','bio','contact','link')

class UploadProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title','image','description','link',)     
        

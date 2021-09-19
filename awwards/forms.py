from django import forms
from .models import Project,Profile

class ProjectForm(forms.Form):
    class Meta:
        model = Project
        fields = ('title','image','description','link','profile','create_date')

class ProfileForm(forms.Form):
    class Meta:
        model = Profile
        fields = ('user','photo','bio','contact','link')
        

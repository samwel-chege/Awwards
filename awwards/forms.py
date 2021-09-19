from django import forms
from .models import Project,Profile

class ProjectForm(forms.Form):
    class Meta:
        model = Project
        fields = ('title','image','description','link','profile','create_date')

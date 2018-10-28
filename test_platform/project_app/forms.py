from django  import forms
from .models import Project,Module

class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['create_time']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','describe']

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        exclude = ['create_time']
from django import forms
from django.forms import ModelForm
from .models import *

class ProjectForm(ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
    class Meta:
        model = Project
        # fields = ['tags',]
        fields = '__all__'

class ImageForm(ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = Image
        fields = ('image', )

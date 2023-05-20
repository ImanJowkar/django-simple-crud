from django import forms
from . import models

class TodoCreateForm(forms.Form):
    title = forms.CharField(label='title')
    body = forms.CharField(label='body')
    created = forms.DateTimeField(label='time')
    
    
class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Todo
        fields = ('title', 'body', 'created')
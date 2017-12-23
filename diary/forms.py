from django import forms

from .models import Category, Tag, Note, Diary

class NoteForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'제목',
        }
    ))
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'기록, 기록 또 기록',
        }
    ))
    
    class Meta:
        model = Note
        fields = ['title','content']

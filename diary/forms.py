from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextField

from .models import Category, Tag, Note, Diary

class NoteForm(forms.ModelForm):
    tags = forms.CharField(required=False,widget=forms.TextInput(
						attrs={
							'class':'form-control',
							'placeholder':'컴마로 구분해서 태그를 작성하세요.'
						}))
    class Meta:
        model = Note
        fields = ['category','title','tags','content',]
        widgets = {
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'제목',
            }),
            'content':SummernoteWidget(attrs={
                'class':'form-control',
                'placeholder':'기록, 기록 또 기록..',
            }),
        }

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title','content',]
        widgets = {
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'제목',
            }),
            'content': SummernoteWidget(attrs={
                'class':'form-control',
                'placeholder':'기록, 기록 또 기록..',
            }),
        }



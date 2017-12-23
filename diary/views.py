from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from .models import Category, Tag, Note, Diary
from .forms import NoteForm

class Index(View):
    def get(self,request):
        return render(request, 'diary/index.html') 

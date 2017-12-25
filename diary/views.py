from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from .models import Category, Tag, Note, Diary
from .forms import NoteForm, DiaryForm

def Index(request):
    return render(request, 'diary/index.html')

class DiaryPage(View):
    def get(self,request):
        diarys = Diary.objects.all()
        form = DiaryForm()

        return render(request, 'diary/diary.html', {
            'type':"diary",
            'diarys':diarys,
            'form':form,
        })

    def post(self,request):
        form = DiaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('diary:diary')

class DiaryDetail(View):
    def get(self,request,pk):
        diary = Diary.objects.get(pk=pk)
        form = DiaryForm(instance=diary)
        return render(request,'diary/diary_detail.html', {'diary':diary, 'form':form})

    def post(self,request,pk):
        diary = Diary.objects.get(pk=pk)
        form = DiaryForm(request.POST, request.FILES, instance=diary)
        referer = request.META.get('HTTP_REFERER')
        if form.is_valid():
            form.save()
            return redirect(referer)

class DiaryDelete(View):
    def get(self,request,pk):
        diary = Diary.objects.get(pk=pk)
        diary.delete()
        return redirect('diary:diary')


class NotePage(View):
    def get(self,request):
        notes = Note.objects.select_related('category').prefetch_related('tags').all()
        form = NoteForm()

        return render(request,'diary/note.html',{
            'type':"note",
            'notes':notes,
            'form':form,
        })
    def post(self,request):
        pass

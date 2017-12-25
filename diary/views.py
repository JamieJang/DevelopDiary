from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.http import HttpResponse

from .models import Category, Tag, Note, Diary
from .forms import NoteForm, DiaryForm

def Index(request):
    return render(request, 'diary/index.html')

class DiaryPage(View):
    def get(self,request):
        diary_list = Diary.objects.all()
        form = DiaryForm()
        paginator = Paginator(diary_list, 18) 

        cur_page = request.GET.get('page')
        try:
            diarys = paginator.page(cur_page)
        except PageNotAnInteger:
            diarys = paginator.page(1)
        except EmptyPage:
            diarys = paginator.page(last_page)
            

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
        note_list = Note.objects.select_related('category').prefetch_related('tags').all()
        category_list = Category.objects.all()
        form = NoteForm()
        paginator = Paginator(note_list, 18) 

        cur_page = request.GET.get('page')
        try:
            notes = paginator.page(cur_page)
        except PageNotAnInteger:
            notes = paginator.page(1)
        except EmptyPage:
            notes = paginator.page(last_page)
            

        return render(request, 'diary/note.html', {
            'type':"note",
            'notes':notes,
            'form':form,
            'category_list':category_list,
        })

    def post(self,request):
        form = NoteForm(request.POST,request.FILES)
        if form.is_valid():
            category = Category.objects.get(pk=request.POST.get('category'))
            title = request.POST.get('title')
            content = request.POST.get('content')
            raw_tags = request.POST.get('tags').split(',')
            note = Note(category=category,title=title,content=content)
            note.save()
            for tag in raw_tags:
                tag = tag.strip().replace(' ','_')
                t = Tag.objects.get_or_create(name=tag)
                t[0].save()
                note.tags.add(t[0])

            return redirect("diary:note")
        else:
            return redirect(request.META.get('HTTP_REFERER'))

class NoteDetail(View):
    def get(self,request,pk):
        note = Note.objects.select_related('category').prefetch_related('tags').get(pk=pk)
        form = NoteForm(instance=note)
        return render(request,'diary/note_detail.html', {'note':note,'form':form})

    def post(self,request,pk):
        note = Note.objects.select_related('category').prefetch_related('tags').get(pk=pk)
        form = NoteForm(request.POST, request.FILES, instance=note)
        referer = request.META.get('HTTP_REFERER')
        if form.is_valid():
            form.save()
            return redirect(referer)

class NoteDelete(View):
    def get(self,request,pk):
        note = Note.objects.select_related('category').prefetch_related('tags').get(pk=pk)
        note.delete()
        return redirect("diary:note")

class NoteByCategory(View):
    def get(self,request,name):
        notes = Note.objects.select_related('category').prefetch_related('tags').\
                filter(category__name=name)
        category_list = Category.objects.all()
        form = NoteForm()

        return render(request,'diary/note.html',{
            'type':"note",
            'notes':notes,
            'category_list':category_list,
            'form':form,
        })

    def post(self,request,name):
        form = NoteForm(request.POST,request.FILES)
        referer = request.META.get('HTTP_REFERER')
        if form.is_valid():
            category = Category.objects.get(pk=request.POST.get('category'))
            title = request.POST.get('title')
            content = request.POST.get('content')
            raw_tags = request.POST.get('tags').split(',')
            note = Note(category=category,title=title,content=content)
            note.save()
            for tag in raw_tags:
                tag = tag.strip().replace(' ','_')
                t = Tag.objects.get_or_create(name=tag)
                t[0].save()
                note.tags.add(t[0])

        return redirect(referer)


class NoteByTags(View):
    def get(self,request,name):
        notes = Note.objects.select_related('category').prefetch_related('tags').filter(tags__name__icontains=name)
        category_list = Category.objects.all()
        form = NoteForm()

        return render(request,'diary/note.html',{
            'type':"note",
            'notes':notes,
            'category_list':category_list,
            'form':form,
        })
    def post(self,request,name):
        form = NoteForm(request.POST,request.FILES)
        referer = request.META.get('HTTP_REFERER')
        if form.is_valid():
            category = Category.objects.get(pk=request.POST.get('category'))
            title = request.POST.get('title')
            content = request.POST.get('content')
            raw_tags = request.POST.get('tags').split(',')
            note = Note(category=category,title=title,content=content)
            note.save()
            for tag in raw_tags:
                tag = tag.strip().replace(' ','_')
                t = Tag.objects.get_or_create(name=tag)
                t[0].save()
                note.tags.add(t[0])

        return redirect(referer)


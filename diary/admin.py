from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Category, Tag, Note, Diary

admin.site.register(Category)
admin.site.register(Tag)

@admin.register(Note)
class NoteAdmin(SummernoteModelAdmin):
    list_display = ['id','title','category','created_at','updated_at']
    list_display_links = ['id','title']

@admin.register(Diary)
class DiaryAdmin(SummernoteModelAdmin):
    list_display = ['id','title','created_at','updated_at']
    list_display_links = ['id','title']


from django.urls import path, re_path, include

from . import views

app_name='diary'

urlpatterns = [
    re_path(r'^$', views.Index, name='diary_index'),
    re_path(r'^diary/',views.DiaryPage.as_view(), name="diary"),
    re_path(r'^note/',views.NotePage.as_view(), name="note"),
]

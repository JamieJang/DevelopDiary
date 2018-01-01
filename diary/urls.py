from django.urls import path, re_path, include

from . import views

app_name='diary'

urlpatterns = [
    re_path(r'^$', views.Index, name='diary_index'),

    re_path(r'^diary/$',views.DiaryPage.as_view(), name="diary"),
    path('diary/detail/<int:pk>/',views.DiaryDetail.as_view(), name='diary-detail'),
    path('diary/delete/<int:pk>/',views.DiaryDelete.as_view(), name="diary-delete"),

    re_path(r'^note/$',views.NotePage.as_view(), name="note"),
    path('note/detail/<int:pk>/',views.NoteDetail.as_view(),name="note-detail"),
    path('note/delete/<int:pk>/', views.NoteDelete.as_view(), name="note-delete"),
    path('note/category/<str:name>/', views.NoteByCategory.as_view(), name="note-category"),
    path('note/tag/<str:name>/',views.NoteByTags.as_view(),name="note-tags"),

    path('note/<str:query>/',views.SearchNote.as_view(), name="search-note"),
]

from django.urls import path, re_path, include

from . import views

app_name='diary'

urlpatterns = [
    path('', views.Index.as_view(), name='diary_index'),
]

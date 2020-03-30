from django.urls import path, re_path
from notes_app import views

app_name = 'notes_app'

urlpatterns = [
    path("", views.NoteListView.as_view(), name='list'),
    re_path(r'^(?P<pk>\d+)/$', views.NoteDetailView.as_view(), name='detail'),
    re_path(r'^create/$', views.NoteCreateView.as_view(), name='create'),
    re_path(r'^update/(?P<pk>\d+)/$', views.NoteUpdateView.as_view(), name='update'),
    re_path(r'^delete/(?P<pk>\d+)/$', views.NoteDeleteView.as_view(), name='delete'),
]

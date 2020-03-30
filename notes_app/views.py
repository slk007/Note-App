from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                 TemplateView, CreateView,
                                 UpdateView, DeleteView)

# Create your views here.

class NoteListView(ListView):
    model  = models.Note        # returns note_list to template

class NoteDetailView(DetailView):
    model = models.Note         # returns note to template
    template_name = 'notes_app/note_detail.html'

class NoteCreateView(CreateView):
    fields = ('title', 'content')
    model = models.Note

class NoteUpdateView(UpdateView):
    fields = ('title', 'content')
    model = models.Note

class NoteDeleteView(DeleteView):
    model = models.Note
    success_url = reverse_lazy("notes_app:list")
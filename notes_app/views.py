from django.shortcuts import render, redirect
from . import models
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.views.generic import (ListView, DetailView,
                                 TemplateView, CreateView,
                                 UpdateView, DeleteView)

# Create your views here.

# for home page
def homeview(request):
    return render(request, "notes_app/home.html", {})

# for loging in a user
def login_user(request):
    # if person has posted the data do this
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # print(username, password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You are logged in!"))
            return redirect('notes_app:list')
        else:
            messages.success(request, ("Error Logging In, Please try again"))
            return redirect('login')
    else:
        # if person is just viewing the page show this
        return render(request, "notes_app/login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have logged out successfully!"))
    # Redirect to a success page.
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("You are registered!"))
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'notes_app/register.html', context)


# def register_user(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request,("You are registered!"))
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     context = {'form': form}
#     return render(request, 'notes_app/register.html', context)


# note list
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
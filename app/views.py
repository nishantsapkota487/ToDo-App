from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView
from .models import ToDoList
from django.http import HttpResponseRedirect
# Create your views here.

class DisplayList(ListView):
    context_object_name = 'tasks'
    model = ToDoList
    template_name = 'homepage.html'

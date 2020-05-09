from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView
from .models import ToDoList
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
# Create your views here.

class homepage(TemplateView):
    template_name = 'index.html'

class DisplayList(ListView):
    context_object_name = 'tasks'
    model = ToDoList
    template_name = 'lists.html'


def index(request):
    return reverse_lazy('index')

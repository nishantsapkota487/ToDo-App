from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView
from .models import ToDoList
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.urls import reverse, reverse_lazy
# Create your views here.



def homepage(request):
    tasks = ToDoList.objects.all()
    return render(request, 'homepage.html', {'tasks': tasks})


def add_task(request):
    already_in_db = []
    tasks = ToDoList.objects.all()
    task = request.POST['task']
    task = task.strip()
    for i in tasks:
        already_in_db.append(i.task)
    if task not in already_in_db:
        if task != "":
            ToDoList.objects.create(
            task = task
            )
    tasks = ToDoList.objects.all()
    return render(request, 'homepage.html', {'tasks': tasks})

def delete_task(request, id):
    tasks = ToDoList.objects.all()
    task_to_delete = ToDoList.objects.get(id = id)
    task_to_delete.delete()
    return render (request, 'homepage.html', {'tasks': tasks})

def check(request):
    user_value = request.GET.get('user_value')
    tasks = ToDoList.objects.all()
    for i in tasks:
        if i.task == user_value:
            return JsonResponse({
                'message': 'Task already exists'
                })
    return reverse_lazy('add_task')

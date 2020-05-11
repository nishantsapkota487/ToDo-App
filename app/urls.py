from django.urls import path
from app.views import  homepage, add_task, delete_task, check
urlpatterns = [
    path('', homepage, name = 'index'),
    path('add/', add_task, name = 'add_task'),
    path('delete/<int:id>', delete_task, name = 'delete_task'),
    path('check/', check, name = 'check')
]

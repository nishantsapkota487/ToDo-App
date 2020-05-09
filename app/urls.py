from django.urls import path
from app.views import  DisplayList
urlpatterns = [
    path('', DisplayList.as_view(), name = 'index'),
]

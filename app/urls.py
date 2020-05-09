from django.urls import path
from app.views import homepage, DisplayList
urlpatterns = [
    path('', homepage.as_view(), name = 'index'),
    path('show/', DisplayList.as_view(), name = 'list'),
]

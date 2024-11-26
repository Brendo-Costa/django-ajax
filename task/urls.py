"""Use to create routes for task app."""
from django.urls import path
from .views import CreateTask, IndexTask


app_name = 'task'


urlpatterns = [
    path('all/', IndexTask.as_view(), name='index'),
    path('create/', CreateTask.as_view(), name='create'),
]



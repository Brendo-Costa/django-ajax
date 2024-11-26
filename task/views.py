from django.http import JsonResponse
from django.shortcuts import render
from .models import Task
from django.views import View


""" def home(request):
    tasks = Task.objects.all()
    return render(request, 'task_app/home.html', {'tasks': tasks})


def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title', None)
        if title:
            task = Task.objects.create(title=title)
            return JsonResponse({'id': task.id, 'title': task.title, 'completed': task.completed})
    return JsonResponse({'error': 'Invalid request'}, status=400) """


class IndexTask(View):
    def get(self, request):
        tasks = Task.objects.all()
        context = {
            'tasks': tasks,
        }
        return render(request, 'task_index.html', context=context)


class CreateTask(View):
    def post(self, request):
        title = request.POST.get('title', None)
        if title:
            task = Task.objects.create(title=title)
            return JsonResponse({'id': task.id, 'title': task.title, 'completed': task.completed})
        else:
            return JsonResponse({'error': 'Invalid request'}, status=400)

from django.shortcuts import render, redirect
from django.views import View
from .models import Task
from .forms import TaskForm

class IndexView(View):
    def get(self, request):
        todo_list = Task.objects.all()
        incomplete_tasks = todo_list.filter(complete=False)
        complete_tasks = todo_list.filter(complete=True)
        context = {
            "incomplete_tasks": incomplete_tasks,
            "complete_tasks": complete_tasks
        }
        return render(request, "mytodo/index.html", context)

class AddView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, "mytodo/add.html", {'form': form})
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(request, "mytodo/add.html", {'form': form})

class UpdateTaskComplete(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')
        if task_id:
            task = Task.objects.get(id=task_id)
            task.complete = not task.complete
            task.save()
        return redirect('/')

class EditTaskView(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        form = TaskForm(instance=task)
        return render(request, 'mytodo/edit_task.html', {'form': form, 'task': task})
    
    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'mytodo/edit_task.html', {'form': form, 'task': task})

class DeleteTaskView(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get("task_id")
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('/')

index = IndexView.as_view()
add = AddView.as_view()
Update_Task_Complete = UpdateTaskComplete.as_view()
edit = EditTaskView.as_view()
delete_task = DeleteTaskView.as_view()

from django.shortcuts import render, redirect
from .models import Task
from django.views import View


class TaskList(View):
    """
        Create and get tasks items
    """

    def get(self, request):
        tasks = Task.objects.all().order_by("-updated")
        context = {"tasks": tasks}
        return render(request, "todo/index.html", context)


    def post(self, request):
        task = Task.objects.create(
            body=request.POST.get("body")
        )
        task.save()

        return redirect('tasks')



class TaskDetail(View):
    """
        View a single task and update single task.
    """

    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        context = {"task":task}

        return render(request, "todo/task.html", context)


    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.body = request.POST.get("body")
        task.save()

        return redirect("tasks")



class DeleteTask(View):
    """
      Delete a task
    """
    def get(self, request, pk):
        task  = Task.objects.get(id=pk)
        context = {"task": task}

        return render(request, "todo/delete.html", context)

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete()

        return redirect("tasks")

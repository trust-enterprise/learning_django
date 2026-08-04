from django.shortcuts import render, redirect 
from todolist.models import Task
from todolist.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
# from django.http import HttpResponse, JsonResponse

def homepage(request):
    return render(request, "main.html", {})

# Create your views here.
def todolist(request):
    # data = {"name": "chanchal", "location": "mau"}
    # return HttpResponse("<h1>this is my response</h1>")
    # return JsonResponse(data)
    
    if request.method == "POST":
        form_data = TaskForm(request.POST or None)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Task added successfully")
            return redirect("todolist")
        messages.success(request, "Something went wrong")

    all_tasks = Task.objects.all()
    paginator = Paginator(all_tasks, 5)
    page = request.GET.get("page")
    all_tasks = paginator.get_page(page)
    context = {
            'page': 'Task List',
            'all_tasks': all_tasks,

        }
    return render(request, "todolist.html", context)

def edit_task(request, task_id):
    task_obj = Task.objects.get(id = task_id)

    if request.method == "POST":
        form_data = TaskForm(request.POST or None, instance = task_obj)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, f"Task has been updated successfully")
            return redirect("todolist")
        messages.success(request, "Error in updating task")

    context = {
        "task_obj": task_obj,
    }
    return render(request, "edit.html", context)

def completed_task(request, task_id):
    task_obj = Task.objects.get(id = task_id)
    task_obj.is_completed = True
    task_obj.save()
    messages.success(request, "Status changed")
    return redirect("todolist")

def pending_task(request, task_id):
    task_obj = Task.objects.get(id = task_id)
    task_obj.is_completed = False
    task_obj.save()
    messages.success(request, "Status changed")
    return redirect("todolist")


def delete_task(request, task_id):
    task_obj = Task.objects.get(id = task_id)
    task_obj.delete()
    messages.success(request, f"Task {task_obj.task} has been deleted")
    return redirect("todolist")

def contact(request):
    context = {
            'page': 'Contact'
        }
    return render(request, "contact.html", context)

def about(request):
    context = {
            'page': 'About'
        }
    return render(request, "about.html", context)





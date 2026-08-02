from django.shortcuts import render
from todolist.models import Task

# from django.http import HttpResponse, JsonResponse

def homepage(request):
    context = { 
        'page': 'Homepage'
    }
    return render(request, "main.html", context)

# Create your views here.
def todolist(request):
    # data = {"name": "chanchal", "location": "mau"}
    # return HttpResponse("<h1>this is my response</h1>")
    # return JsonResponse(data)
    
    all_tasks = Task.objects.all()
    context = {
            'page': 'Task List',
            'all_tasks': all_tasks,
        }
    return render(request, "todolist.html", context)



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





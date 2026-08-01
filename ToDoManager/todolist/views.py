from django.shortcuts import render

# from django.http import HttpResponse, JsonResponse

def homepage(request):
    return render(request, "main.html", {})

# Create your views here.
def todolist(request):
    # data = {"name": "chanchal", "location": "mau"}
    # return HttpResponse("<h1>this is my response</h1>")
    # return JsonResponse(data)
    return render(request, "todolist.html", {})


def contact(request):
    return render(request, "contact.html", {})

def about(request):
    return render(request, "about.html", {})





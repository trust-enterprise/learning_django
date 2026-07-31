from django.shortcuts import render

# from django.http import HttpResponse, JsonResponse


# Create your views here.
def todolist(request):
    # data = {"name": "chanchal", "location": "mau"}
    # return HttpResponse("<h1>this is my response</h1>")
    # return JsonResponse(data)
    return render(request, "main.html", {})

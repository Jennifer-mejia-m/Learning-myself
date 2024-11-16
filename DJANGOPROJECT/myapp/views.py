#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render

def index(request):
    title = "Django course!!"
    return render(request,'index.html', {
        'title':title
    })

def aboutt(request):
    return render(request, 'about1.html')

def hello(request, username):
    #print(username)
    return HttpResponse("<h2> Hello %s</h2>" % username)

def about(request, id):
    result = id + 100 * 2
    return HttpResponse(f"About {result}")

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects':projects
    })

def tasks(request, id):
    #task = Task.objects.get(id = id)
    taski = get_object_or_404(Task, id=id) #para que aparezca el código de error si no existe el objeto
    return HttpResponse("task: %s" % taski.title)


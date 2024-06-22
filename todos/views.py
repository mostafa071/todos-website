from django.shortcuts import render , HttpResponse
from django.views.decorators.http import require_http_methods

# Create your views here.
from todos.models import Todos


def index(request):
    todos = Todos.objects.all()
    
    return render(request , 'todos/todos.html' , {'todos': todos})

require_http_methods(['POST'])
def add_todo(request):
    todo = None
    title = request.POST.get('title' , ' ')
    if title:
        todo = Todos.objects.create(title = title)
    return render(request , 'todos/partials/todo.html' , {'todo' : todo})

require_http_methods(["PUT"])

def update_todo(request , pk):
    todo = Todos.objects.get(pk=pk)
    todo.is_done = True
    todo.save()
    
    return render(request , 'todos/partials/todo.html' , {'todo' : todo})

require_http_methods(["DELETE"])

def delete(request,pk):
    todo = Todos.objects.get(pk=pk)
    
    todo.delete()
    return HttpResponse()
    
        
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect

from tasks.models import *
from tasks.forms import *
# Create your views here.
def index(request):
    tasks=Task.objects.filter(uname='abc')
    form =TaskForm()
    #print(tasks)
    if request.method=='POST':
        #tasks=Task.objects.all()
        xyz=dict(request.POST)
        xyz['uname']='abc'
        xyz['title']=xyz['title'][0]
        print(xyz)
        #print(request.POST, "  ", type(request.POST['title']))
        form =TaskForm(xyz)
        #print(form)
        if form.is_valid():
            form.save()
            #print(form, "  ", type(form))
            return redirect('/index')
    for j in form:
        print('123   ', j)
    #print(tasks)
    #abc=[(9, 'Vidush', '', 'Django'), (10, 'Vidush', '', 'bell')]
    context={'tasks':tasks, 'form':form}
    #print(tasks)
    return render(request, 'tasks/list.html', context)
def updateTask(request,pk):
    task=Task.objects.get(id=pk)

    form =TaskForm(instance=task)
    
    if request.method=='POST':
        form =TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/index')
    context={'form' : form}
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    item=Task.objects.get(pk)
    context={'item':item}
    return render(request, 'tasks/delete.html')
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect

from tasks.models import Task
from tasks.forms import *
# Create your views here.
def index(request, uname):
    form =TaskForm()
    tasks=Task.objects.all()
    print(uname)
    if request.method=='POST':
        #tasks=Task.objects.all()
        print(request.POST, "  ", type(request.POST['title']))
        form =TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index/'+uname)
    #for j in tasks:
        #print('123   ', j.created  )
    #print(tasks)
    abc=[(9, 'Vidush', '', 'Django'), (10, 'Vidush', '', 'bell')]
    context={'tasks':tasks, 'form':form}
    #print(tasks)
    return render(request, 'tasks/list.html', context)
def signin2(request, uname):
    print(uname)
    return HttpResponse(uname)
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect

from tasks.models import *
from tasks.forms import *
# Create your views here.
def index(request):
    tasks=Task.objects.all()
    form =TaskForm()
    print(tasks)
    if request.method=='POST':
        #tasks=Task.objects.all()
        #print(request.POST, "  ", type(request.POST['title']))
        form =TaskForm(request.POST)
        #print(form)
        if form.is_valid():
            form.save()
            print(form, "  ", type(form))
            return redirect('/index')
    for j in form:
        print('123   ', j)
    #print(tasks)
    #abc=[(9, 'Vidush', '', 'Django'), (10, 'Vidush', '', 'bell')]
    context={'tasks':tasks, 'form':form}
    #print(tasks)
    return render(request, 'tasks/list.html', context)  
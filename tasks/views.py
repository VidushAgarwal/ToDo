from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect

from tasks.models import *
from tasks.forms import *
# Create your views here.
def index(request):
    f=open("user.user", 'r')
    u=f.read()
    print(u)
    f.close()
    tasks=Task.objects.filter(uname=u)
    form =TaskForm()
    #print(tasks)
    if request.method=='POST':
        #tasks=Task.objects.all()
        xyz=dict(request.POST)
        print(xyz)
        if 'title' in xyz.keys():
            xyz['title']=xyz['title'][0]
            xyz['uname']=u
        #print(xyz)
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
def deleteTask(request, pk):
    item=Task.objects.get(id=pk)
    #print(pk)
    d=Task.objects.filter(id=pk).delete()
    context={'item':item}
    return render(request, 'tasks/delete.html')
def logout(request):
    print("logout")
    f=open('user.user', 'w')
    f.write('q')
    f.close()
    return redirect('/')
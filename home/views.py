import email
from django.shortcuts import render, HttpResponse, redirect
from home.models import data
from tasks.urls import *
from tasks.views import index
from tasks.models import Task
# Create your views here.
def homepage(request):
    return render(request, 'home.html')
def signin(request):
    if request.method=='POST':
        #print(request.POST)
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        print('abc ',uname)
        f=0
        a=data.objects.all()
        b=data.objects.filter(uname=uname)
        for j in b:
            #print("    ", j.passw)
            if passw==j.passw:
                f=1
        for i in a:
            if uname == i.uname and f==1:
                #print("1234567890")
                return redirect('/index')
        #print(type(i.uname), i.uname)
        Data=data(uname=uname, passw=passw)
        return redirect('/')
def signup(request):
    if request.method=='POST':
        #print(request.POST)
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        passw=request.POST.get('passw')
        a=data.objects.all()
        '''for i in a:
            if uname == i.uname:
                return redirect('/')'''
        Data=data(uname=uname, passw=passw, email=email)
        Data.save()
        return redirect('/index/'+uname)
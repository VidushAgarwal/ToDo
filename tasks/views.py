from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from tasks.models import *
from tasks.forms import *
# Create your views here.
def index(request):
    tasks=Task.objects.all()
    form =TaskForm()
    context={'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html', context)

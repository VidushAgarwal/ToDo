from django.shortcuts import render, HttpResponse
from home.models import data
# Create your views here.
def homepage(request):
    return render(request, 'home.html')
def first(request):
    if request.method=='POST':
        print(request.POST['submit'])
        uname=request.POST.get('uname')
        Data=data(uname=uname)
        Data.save()
    return HttpResponse("hello")
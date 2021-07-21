from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):

    if request.method =="POST":
        return render(request, 'accountapp/hello_world.html', context={'text_1':"POST METHOD!!"})

    if request.method =="GET":
        return render(request, 'accountapp/hello_world.html', context={'text_1':"GET METHOD!!"})
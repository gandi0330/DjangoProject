from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):

    if request.method =="POST":
        temp = request.POST.get('hello_world_input')

        hello_world_model1 = HelloWorld()
        hello_world_model1.text = temp
        hello_world_model1.save()

        return render(request, 'accountapp/hello_world.html', context={'hello_world_output':hello_world_model1})

    if request.method =="GET":
        return render(request, 'accountapp/hello_world.html', context={'text_1':"GET METHOD!!"})
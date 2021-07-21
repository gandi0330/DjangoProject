from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):

    if request.method =="POST":
        temp = request.POST.get('hello_world_input')

        hello_world_model1 = HelloWorld()
        hello_world_model1.text = temp
        hello_world_model1.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    if request.method =="GET":
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list':hello_world_list})
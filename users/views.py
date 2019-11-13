from django.http import HttpResponse
from django.shortcuts import render

from .models import Users


def login(request):
    context = {}
    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if Users.objects.filter(username=username, password=password):
            user = Users.objects.get(username=username, password=password)
            context['user'] = user
    return render(request, 'users/login.html', context)


def register(request):
    context = {}
    if request.method == "POST":
        Users.objects.create(username=request.POST['username'], password=request.POST['password'])
        context['message'] = 'OK'
    return render(request, 'users/register.html', context)

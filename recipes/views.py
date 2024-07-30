from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render (request, 'recipes/home.html')

def contato(request):
    return HttpResponse('WELCOME TO CONTATO 📱')

def sobre(request):
    return HttpResponse('WELCOME TO SOBRE 🗃️')
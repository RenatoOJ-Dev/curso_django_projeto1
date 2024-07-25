from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse ('WELCOME TO HOME 🏠')

def contato(request):
    return HttpResponse('WELCOME TO CONTATO 📱')

def sobre(request):
    return HttpResponse('WELCOME TO SOBRE 🗃️')
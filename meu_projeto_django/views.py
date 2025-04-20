
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path, include


def index_view(request):
    return HttpResponse("Página Inicial do meu projeto Django!")

def sobre_view(request):
    return HttpResponse("Sobre o meu projeto Django!")


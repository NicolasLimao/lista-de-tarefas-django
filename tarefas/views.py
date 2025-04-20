from .forms import TarefaForm
from .models import TarefaModel
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.http import request

def tarefas_view(request):
    contexto = {
        'nome': 'João',
        'tarefas' : TarefaModel.objects.all()

    }
    return render(request, 'tarefas/home.html', contexto)

def tarefas_adicionar(request:HttpRequest):
    if request.method == 'POST':
        formulario = TarefaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarefas:home')
  
    
    contexto = {
        "form": TarefaForm
    }
    return render(request, 'tarefas/adicionar.html', contexto)

def tarefas_deletar(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    tarefa.delete()
    return redirect('tarefas:home')

def tarefas_editar(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    if request.method == 'POST':
        formulario = TarefaForm(request.POST, instance=tarefa)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarefas:home')
    else:
        formulario = TarefaForm(instance=tarefa)

    contexto = {
        "form": formulario
    }
    return render(request, 'tarefas/adicionar.html', contexto)
    
   
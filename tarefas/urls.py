from django.urls import path
from . import views

app_name = "tarefas"




urlpatterns = [
    path('', views.tarefas_view, name='home'),
    path('adicionar/', views.tarefas_adicionar, name='adicionar'),
    path('deletar/<int:id>/', views.tarefas_deletar, name='deletar'),
    path('editar/<int:id>/', views.tarefas_editar, name='editar'),
]
from django import forms
from .models import TarefaModel

class TarefaForm(forms.ModelForm):
    class Meta:
        model = TarefaModel
        fields = ['titulo', 'nome', 'descricao', 'concluida']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da tarefa'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da tarefa'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição da tarefa'}),
            'concluida': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'Titulo': 'Título',	
            'nome': 'Nome',
            'descricao': 'Descrição',
            'concluida': 'Concluída',
        }
        help_texts = {
            'Titulo': 'Digite o título da tarefa',
            'nome': 'Digite o nome da tarefa',
            'descricao': 'Digite uma descrição para a tarefa',
            'concluida': 'Marque se a tarefa estiver concluída',
        }
        error_messages = {
            'Titulo': {
                'required': 'Este campo é obrigatório',
                'max_length': 'O título da tarefa não pode ter mais de 100 caracteres',
            },
            'nome': {
                'required': 'Este campo é obrigatório',
                'max_length': 'O nome da tarefa não pode ter mais de 100 caracteres',
            },
            'descricao': {
                'max_length': 'A descrição não pode ter mais de 500 caracteres',
            },
        }
        
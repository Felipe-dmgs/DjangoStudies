from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm

def home(request):

    if request.method == 'POST':
        form = TarefaForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('home')

    else:
        form = TarefaForm()

        todas_as_tarefas = Tarefa.objects.all().order_by('-criada_em')

        context = {
        'nome_usuario': 'Júnior',
        'tecnologias': ['Python', 'Django', 'Models', 'Forms'],
        'tarefas': todas_as_tarefas,
        'form': form,
        }
        return render(request, 'home.html', context)

def concluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa,pk=pk)

    if request.method == 'POST':
        tarefa.concluida = True
        tarefa.save()

        return redirect('home')

def deletar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    
    if request.method == 'POST':
        tarefa.delete()

        return redirect('home')
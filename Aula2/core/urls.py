from django.urls import path
from .views import ListaTarefasAPIView, ContagemTarefasAPIView

app_name = 'core'

urlpatterns = [
    path('tarefa/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
    path('tarefa/contagem/', ContagemTarefasAPIView.get(), name='contar-tarefa')
]


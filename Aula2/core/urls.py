from django.urls import path
from .views import ListaTarefasAPIView

app_name = 'core'

urlpatterns = [
    path('tarefa/', ListaTarefasAPIView.as_view(), name='lista-tarefas')
]


from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    """
    Model para representar uma tarefa de usuário.
    Cada tarefa tem:
    - Um dono (user)
    - Um título
    - Um status de conclusão
    - Data de criação automática
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tarefa',
        verbose_name='Usuário'
    )

    titulo = models.CharField(
        max_length=200,
        verbose_name='Título'
    )

    descricao = models.TextField(
        max_length=400,
        verbose_name='Descrição'
    )

    concluida = models.BooleanField(
        default=False,
        verbose_name='Concluida'
    )

    criada_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criada em'
    )

class Meta:
    """Tipo um docker compose pro models"""

    verbose_name = 'Tarefa'

    verbose_name_plural = 'Tarefas'

    ordering = ['-criada_em'] #O meno faz mostrar do mais atigo pro mais recete

    def __str__(self):
        """Representacao em string (usado no admin)"""
        return f"{self.titulo} ({'<' if self.concluida else 'X'})"
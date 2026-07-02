from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ['id','titulo','user','descricao' ,'concluida', 'criada_em']

    list_filter = ['concluida', 'criada_em']

    search_fields = ['titulo', 'user__username']
    
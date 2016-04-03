from django.contrib import admin
from django.contrib.admin import ModelAdmin

from todo.models import Tarefa


class TarefaAdmin(ModelAdmin):
    list_display = ['nome', 'data_criacao', 'data_execucao', 'executado']
    fields = ['nome', 'descricao', 'executado']
    list_editable = ['executado']

admin.site.register(Tarefa, TarefaAdmin)

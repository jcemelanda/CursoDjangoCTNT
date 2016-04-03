from django.views.generic import ArchiveIndexView
from django.views.generic import DetailView

from todo.models import Tarefa

class TarefasView(ArchiveIndexView):
    model = Tarefa
    date_field = 'data_criacao'


class TarefaDetalhe(DetailView):
    model = Tarefa

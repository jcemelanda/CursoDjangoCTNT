from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic import ArchiveIndexView
from django.views.generic import DetailView
from django.views.generic import View

from todo.models import Tarefa


class TarefasView(ArchiveIndexView):
    model = Tarefa
    date_field = 'data_criacao'


class TarefaDetalhe(DetailView):
    model = Tarefa


class Home(View):
    def __init__(self):
        self.template_name = 'home.html'
        self.context = {}

    def get(self, request, *args, **kwargs):
        self.context['counter'] = Tarefa.objects.filter(executado=False).count()
        return render_to_response(self.template_name, self.context,
                                  RequestContext(request))

from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic import ArchiveIndexView
from django.views.generic import DetailView
from django.views.generic import View

from todo.models import Tarefa
from todo.forms import FormNovoUsuario
from todo.forms import TarefaForm


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


class CriaUserView(View):
    def __init__(self):
        self.template_name = 'todo/cria_usuario.html'
        self.context = {}

    def get(self, request):
        self.context['form'] = FormNovoUsuario()
        return render_to_response(self.template_name, self.context,
                                  RequestContext(request))

    def post(self, request):
        form = FormNovoUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        self.context['form'] = form
        return render_to_response(self.template_name, self.context,
                                  RequestContext(request))


class AdicionaTarefa(View):
    def __init__(self):
        self.template_name = 'todo/cria_tarefa.html'
        self.context = {}

    def get(self, request):
        self.context['form'] = TarefaForm()
        return render_to_response(self.template_name, self.context,
                                  RequestContext(request))

    def post(self, request):
        form = TarefaForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('/todo/tarefas/')
        self.context['form'] = form
        return render_to_response(self.template_name, self.context,
                                  RequestContext(request))

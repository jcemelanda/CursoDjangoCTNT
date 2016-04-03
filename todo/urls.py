from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from todo.views import AdicionaTarefa
from todo.views import CriaUserView
from todo.views import TarefaDetalhe
from todo.views import TarefasView

urlpatterns = [
    url(r'^tarefas/$', login_required(TarefasView.as_view())),
    url(r'^tarefas/(?P<pk>\d+)/$', login_required(TarefaDetalhe.as_view())),
    url(r'^cria_usuario/$', login_required(CriaUserView.as_view())),
    url(r'^tarefas/criar/$', login_required(AdicionaTarefa.as_view())),
]

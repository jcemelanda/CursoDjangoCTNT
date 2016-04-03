from django.conf.urls import url
from todo.views import AdicionaTarefa
from todo.views import CriaUserView
from todo.views import TarefaDetalhe
from todo.views import TarefasView

urlpatterns = [
    url(r'^tarefas/$', TarefasView.as_view()),
    url(r'^tarefas/(?P<pk>\d+)/$', TarefaDetalhe.as_view()),
    url(r'^cria_usuario/$', CriaUserView.as_view()),
    url(r'^tarefas/criar/$', AdicionaTarefa.as_view()),
]

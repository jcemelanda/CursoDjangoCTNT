from datetime import datetime

from django.contrib.auth.models import User
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateField
from django.db.models import ForeignKey
from django.db.models import Model
from django.db.models import TextField
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Tarefa(Model):
    '''
    Classe que representa uma tarefa
    '''
    nome = CharField(max_length=50)
    descricao = TextField(verbose_name='descrição')
    data_criacao = DateField(auto_now_add=True, verbose_name='data de criação')
    data_execucao = DateField(null=True, blank=True, verbose_name='data de execução')
    executado = BooleanField(default=False)
    usuario = ForeignKey(User, verbose_name="usuário")

    class Meta:
        ordering = ['-data_criacao', 'executado']


@receiver(pre_save, sender=Tarefa)
def executa_tarefa(sender, instance, **kwargs):
    if instance.executado:
        instance.data_execucao = datetime.now()
    else:
        instance.data_execucao = None

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import Form
from django.forms import CharField
from django.forms import EmailField
from django.forms import ModelForm
from django.forms import PasswordInput

from todo.models import Tarefa


class FormNovoUsuario(Form):
    nome_de_usuario = CharField()
    nome = CharField(required=False)
    email = EmailField(required=False)
    senha = CharField(widget=PasswordInput)
    repeticao_senha = CharField(widget=PasswordInput)

    def save(self):
        params = {
            'username': self.cleaned_data['nome_de_usuario'],
            'email': self.cleaned_data['email'],
            'password': self.cleaned_data['senha'],
        }
        if self.cleaned_data['nome']:
            params['first_name'] = self.cleaned_data['nome']
        User.objects.create_user(**params)

    def clean_nome_de_usuario(self):
        nome = self.cleaned_data['nome_de_usuario']
        if User.objects.filter(username=nome).exists():
            raise ValidationError('Já existe usuáio com este nome de usuário')
        return nome

    def clean_repeticao_senha(self):
        senha1 = self.cleaned_data['senha']
        senha2 = self.cleaned_data['repeticao_senha']
        if senha1 != senha2:
            raise ValidationError("As senhas devem ser iguais.")
        return senha1


class TarefaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        return super().__init__(*args, **kwargs)

    class Meta:
        model = Tarefa
        fields = ['nome', 'descricao', 'executado']

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        obj = super().save(*args, **kwargs)
        if self.request:
            obj.usuario = self.request.user
        obj.save()
        return obj

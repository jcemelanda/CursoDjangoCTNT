from django.test import TestCase
from django.test import LiveServerTestCase
from django.db.utils import IntegrityError

from todo.models import Tarefa


class CriaTarefaTestCase(TestCase):
    def test_cria_tarefa_vazia(self):
        with self.assertRaises(IntegrityError):
            Tarefa.objects.create()


class HomeTestCase(LiveServerTestCase):
    def test_home_funciona(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_tem_ola(self):
        response = self.client.get('/')
        self.assertContains(response, 'Olá')


class LoginTestCase(TestCase):
    def test_home_tem_link_login(self):
        response = self.client.get('/')
        if response.context['user'].is_authenticated():
            self.assertNotContains(response, "Login")
        else:
            self.assertContains(response, "Login")

    def test_login_volta_para_home(self):
        response = self.client.get('/')
        if not response.context['user'].is_authenticated():
            self.assertContains(response,
                '<a href="/admin/login/?next=/">Login</a>' , html=True)

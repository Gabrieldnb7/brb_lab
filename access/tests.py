# access/tests.py

import os
from django.test import TestCase, Client
from django.urls import reverse

class AcessoViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 1) Garante que o VERIFY_CODE existe no ambiente de teste
        os.environ['VERIFY_CODE'] = 'ABC123'
        # 2) Cria um usuário de teste
        from users.models import Usuario
        cls.user = Usuario.objects.create_user(
            nome='Test User',
            cpf='00000000000',
            email='test@example.com',
            password='1234'
        )

    def setUp(self):
        # Cliente de teste e login
        self.client = Client()
        self.client.login(cpf='00000000000', password='1234')

    def test_get_not_allowed(self):
        """GET em /acesso/ deve retornar 405"""
        response = self.client.get(reverse('registrar_acesso'))
        self.assertEqual(response.status_code, 405)

    def test_missing_fields(self):
        """POST sem 'codigo' ou 'ambiente' → 400 e mensagem de erro"""
        response = self.client.post(reverse('registrar_acesso'), {})
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {'erro': 'codigo e ambiente são obrigatórios'})

    def test_invalid_code(self):
        """POST com 'codigo' errado → 401"""
        response = self.client.post(
            reverse('registrar_acesso'),
            {'codigo': 'WRONG', 'ambiente': 'Sala A'}
        )
        self.assertEqual(response.status_code, 401)
        self.assertJSONEqual(response.content, {'erro': 'código inválido'})

    def test_success(self):
        """POST correto → 201 e objeto criado"""
        response = self.client.post(
            reverse('registrar_acesso'),
            {'codigo': 'ABC123', 'ambiente': 'Sala A'}
        )
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertIn('mensagem', data)
        self.assertIn('idAcesso', data)

        # Verifica que o registro realmente foi salvo
        from access.models import Acesso
        self.assertTrue(Acesso.objects.filter(idAcesso=data['idAcesso']).exists())

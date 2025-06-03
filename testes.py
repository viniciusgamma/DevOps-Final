import unittest
from app import app

class SimpleDifferentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_home_response_type(self):
        # Verifica se o retorno da home é JSON
        response = self.client.get('/')
        self.assertEqual(response.content_type, 'application/json')

    def test_items_list_length(self):
        # Verifica se a lista de itens tem exatamente 3 elementos
        response = self.client.get('/items')
        items = response.get_json().get("items", [])
        self.assertEqual(len(items), 3)

    def test_swagger_ui_available(self):
        # Verifica se a rota do Swagger UI está disponível (deve retornar 200 ou 302)
        response = self.client.get('/swagger/')
        self.assertIn(response.status_code, [200, 302])

if __name__ == '__main__':
    unittest.main()

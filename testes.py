import unittest
from app import app

class SimpleTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_status(self):
        # Verifica se a home retorna 200
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_items_status(self):
        # Verifica se /items retorna 200
        res = self.client.get('/items')
        self.assertEqual(res.status_code, 200)

    def test_not_found(self):
        # Verifica se uma rota inválida retorna 404
        res = self.client.get('/naoexiste')
        self.assertEqual(res.status_code, 404)

if __name__ == '__main__':
    unittest.main()

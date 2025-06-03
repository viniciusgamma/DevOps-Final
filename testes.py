import werkzeug

# Corrige erro do werkzeug
if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "2.3.0"

from app import app
import unittest

class SimpleTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_status(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_items_status(self):
        res = self.client.get('/items')
        self.assertEqual(res.status_code, 200)

    def test_not_found(self):
        res = self.client.get('/naoexiste')
        self.assertEqual(res.status_code, 404)

if __name__ == '__main__':
    unittest.main()

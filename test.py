import unittest
from app import app


class FlaskTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')

    def test_hello(self):
        response = self.app.post('/hello', data={'name': 'John'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, John!', response.data)


if __name__ == '__main__':
    unittest.main()

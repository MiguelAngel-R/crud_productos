import unittest
import json
from backend import app, init_db

class ProductoTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DATABASE'] = ':memory:'  # Usa base de datos en memoria
        self.client = app.test_client()
        with app.app_context():
            init_db()

    def test_post_producto(self):
        nuevo_producto = {
            'nombre': 'Test Producto',
            'precio': 10.5,
            'descripcion': 'Producto de prueba'
        }
        response = self.client.post('/productos',
                                    data=json.dumps(nuevo_producto),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Producto guardado correctamente', response.data)

if __name__ == '__main__':
    unittest.main()

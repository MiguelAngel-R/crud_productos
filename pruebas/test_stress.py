import requests
import time

def test_massive_inserts(n=100):
    for i in range(n):
        producto = {
            "nombre": f"Producto {i}",
            "precio": float(i),
            "descripcion": f"Descripción {i}"
        }
        res = requests.post("http://127.0.0.1:5000/productos", json=producto)
        assert res.status_code == 200
    print(f"Prueba de estabilidad: {n} productos insertados exitosamente")

test_massive_inserts()

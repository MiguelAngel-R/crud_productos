import requests

def test_update_and_delete():
    # Crear producto inicial
    producto = {
        "nombre": "Gorra",
        "precio": 9.99,
        "descripcion": "Gorra negra"
    }
    requests.post("http://127.0.0.1:5000/productos", json=producto)
    productos = requests.get("http://127.0.0.1:5000/productos").json()
    gorra = next((p for p in productos if p["nombre"] == "Gorra"), None)
    assert gorra is not None

    # Actualizar
    update = {
        "nombre": "Gorra modificada",
        "precio": 12.50,
        "descripcion": "Gorra edición limitada"
    }
    res_put = requests.put(f"http://127.0.0.1:5000/productos/{gorra['id']}", json=update)
    assert res_put.status_code == 200

    # Eliminar
    res_del = requests.delete(f"http://127.0.0.1:5000/productos/{gorra['id']}")
    assert res_del.status_code == 200
    print("Prueba de caja gris: producto actualizado y eliminado correctamente")

test_update_and_delete()
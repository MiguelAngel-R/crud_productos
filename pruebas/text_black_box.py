import requests

def test_post_and_get_product():
    # Crear producto
    producto = {
        "nombre": "Camiseta",
        "precio": 19.99,
        "descripcion": "Camiseta de algodón"
    }
    res_post = requests.post("http://127.0.0.1:5000/productos", json=producto)
    assert res_post.status_code == 200

    # Obtener todos los productos
    res_get = requests.get("http://127.0.0.1:5000/productos")
    assert res_get.status_code == 200
    productos = res_get.json()
    assert any(p["nombre"] == "Camiseta" for p in productos)
    print("Prueba de caja negra: producto creado y listado correctamente")

test_post_and_get_product()


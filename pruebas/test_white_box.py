import sys
import os
import sqlite3

# Agregar ruta al backend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend import init_db, get_db, DATABASE

def test_insercion_y_lectura():
    # Asegurar DB limpia
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
    init_db()

    # Insertar producto directamente
    conn = get_db()
    conn.execute("INSERT INTO productos (nombre, precio, descripcion) VALUES (?, ?, ?)",
                 ("Producto Prueba", 99.99, "Producto de prueba desde test"))
    conn.commit()

    # Leer el producto insertado
    cursor = conn.execute("SELECT nombre, precio, descripcion FROM productos WHERE nombre = ?", ("Producto Prueba",))
    row = cursor.fetchone()

    assert row is not None, "No se encontró el producto insertado"
    assert row[0] == "Producto Prueba"
    assert row[1] == 99.99
    assert row[2] == "Producto de prueba desde test"

    print("Prueba de caja blanca: inserción y lectura directa desde DB correctas")

test_insercion_y_lectura()

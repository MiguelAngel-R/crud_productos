import subprocess
import time
import requests

def test_app_runs():
    process = subprocess.Popen(["python", "backend.py"])
    time.sleep(3)  # Esperar a que el servidor arranque

    try:
        response = requests.get("http://127.0.0.1:5000/")
        assert response.status_code == 200
        print("Prueba de humo exitosa: La app respondió correctamente")
    except Exception as e:
        print("Error en prueba de humo:", e)
    finally:
        process.terminate()

test_app_runs()
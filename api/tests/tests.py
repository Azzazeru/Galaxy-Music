import requests
import pytest
# from api.models import Producto, Disco
# from rest_framework.test import APIClient
# from django.urls import reverse

# ENDPOINT = "https://gmad.up.railway.app/api"
ENDPOINT = "http://127.0.0.1:8000/api"

def test_endpoint():
    response = requests.get(f"{ENDPOINT}/public/productos/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_get_productos():    
    response = requests.get(f"{ENDPOINT}/public/productos/")
    data = response.json()
    
    assert response.status_code == 200
    
    assert data[0]['id_producto'] == 1

@pytest.mark.django_db
def test_create_producto_with_authentication():
    # Paso 1: Realizar el login y obtener la sesión
    login_url = f"{ENDPOINT}/login/"  # Ajusta según tu configuración de URLs
    login_data = {
        'username': 'jorgelagosboss',
        'password': 'jorgelagosboss12345'
    }
    session = requests.Session()
    response = session.post(login_url, data=login_data)
    
    # Verificar que el login fue exitoso
    assert response.status_code == 200
    
    # Paso 2: Crear un producto usando la sesión autenticada
    productos_url = f"{ENDPOINT}/hidden/productos/"
    producto_data = {
        'id_producto': 100,
        'disco': 1,
        'precio': 1000,
        'stock': 10,
        'estado': False
    }
    
    # Agregar CSRF token a los headers desde la sesión
    csrf_token = session.cookies['csrftoken']
    headers = {'X-CSRFToken': csrf_token}
    
    # Realizar la solicitud POST con la sesión autenticada
    response = session.post(productos_url, json=producto_data, headers=headers)
    
    # Verificar que se creó el producto correctamente
    assert response.status_code == 201
    
    # Puedes hacer más verificaciones según lo que esperes en la respuesta JSON
    # Por ejemplo, verificar que el producto se haya creado correctamente
    
    # Obtener los productos y verificar que el nuevo producto está presente
    response = requests.get(productos_url)
    assert response.status_code == 200
    data = response.json()
    assert any(producto['id_producto'] == 1 for producto in data)

    Paso 1: Realizar el login y obtener la sesión

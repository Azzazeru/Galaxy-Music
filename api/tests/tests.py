import requests
import pytest
from api.models import Producto, Disco
from rest_framework.test import APIClient
from django.urls import reverse

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


import requests

ENDPOINT = "https://gmad.up.railway.app/api"

def create_task(payload):
    return request.put(f"{ENDPOINT}/public/productos/")

def test_can_call_endpoint():
    response = requests.get(f"{ENDPOINT}/public/productos/")
    assert response.status_code == 200

def test_can_list_products():
    for _ in range(3):
        payload = new_task_payload()
        create_task_response = create_task(payload)
        assert = create_task_response.status_code == 200
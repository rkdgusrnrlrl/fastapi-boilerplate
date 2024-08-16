from starlette.testclient import TestClient


def test_get_products(client: TestClient):
    response = client.get("/products")
    assert response.status_code == 200
    response_json = response.json()
    assert 'items' in response_json
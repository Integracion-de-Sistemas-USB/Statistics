from fastapi.testclient import TestClient
import os 
import sys 
import pytest
from httpx import AsyncClient
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import app

sample_data = {
    "id": "test_id",
    "name": "Sample Name",
    "x": 10.0,
    "y": 20.0,
    "scenary": {
        "bullet_weight": 5.0,
        "distance": 100.0,
        "ammo": "Sample Ammo",
        "temperature": 25.0,
        "altitude": 500.0,
        "humidity": 50.0,
        "scenary": "Sample Scenary",
        "stress_level": 3,
        "caliber": 0.45
    }
}

client = TestClient(app)

@pytest.mark.anyio
async def test_get_results(client: AsyncClient):
    response = await client.get("/results/")
    assert response.status_code == 200

    assert response.json()["code"] == 200
    assert response.json()["status"] == "Ok"
    assert response.json()["message"] == "Success retrieve all data"

    results_list = response.json()["result"]
    assert isinstance(results_list, list)

@pytest.mark.anyio
async def test_create_results(client: AsyncClient):
    response = await client.post("/results/create", json=sample_data)
    
    assert response.status_code == 200
    assert response.json()["code"] == 200
    assert response.json()["status"] == "Ok"
    assert response.json()["message"] == "Success created data"

@pytest.mark.anyio 
async def test_retrieve_by_id_results(client: AsyncClient):
    response = await client.get("/results/test_id")
    assert response.json()["code"] == 200
    assert response.json()["status"] == "Ok"
    assert response.json()["message"] == "Success get data"

    result = response.json()["result"]
    assert result["_id"] == "test_id"
    assert result["name"] == "Sample Name"
    assert result["x"] == 10
    assert result["y"] == 20
    
    scenary = result["scenary"]
    assert scenary["bullet_weight"] == 5
    assert scenary["distance"] == 100
    assert scenary["ammo"] == "Sample Ammo"
    assert scenary["temperature"] == 25
    assert scenary["altitude"] == 500
    assert scenary["humidity"] == 50
    assert scenary["scenary"] == "Sample Scenary"
    assert scenary["stress_level"] == 3
    assert scenary["caliber"] == 0.45

@pytest.mark.anyio
async def test_update_result(client: AsyncClient):
    response = await client.put("results/update/test_id", json={"name": "Pedro"})
    assert response.json()["code"] == 200
    assert response.json()["status"] == "Ok"
    assert response.json()["message"] == "Success update data"

    response = await client.get("/results/test_id")
    result = response.json()["result"]
    assert result["name"] == "Pedro"

@pytest.mark.anyio
async def test_delete_id_result(client: AsyncClient): 
    response = await client.delete("/results/delete/test_id")
    assert response.json()["code"] == 200
    assert response.json()["status"] == "Ok"
    assert response.json()["message"] == "Success delete data"

    response = await client.get("/results/test_id")
    with pytest.raises(KeyError) as e: 
        response.json()["result"]
    
    assert str(e.value) == "\'result\'"

@pytest.mark.anyio
async def test_retrieve_nonexistent_id(client: AsyncClient):
    response = await client.get("/results/nonexistent_id")
    assert response.status_code == 404
    assert response.json()["code"] == 404
    assert response.json()["status"] == "Not Found"
    assert response.json()["message"] == "Data not found"

@pytest.mark.anyio
async def test_update_nonexistent_id(client: AsyncClient):
    response = await client.put("/results/update/nonexistent_id", json={"name": "Updated Name"})
    assert response.status_code == 404
    assert response.json()["code"] == 404
    assert response.json()["status"] == "Not Found"
    assert response.json()["message"] == "Data not found"

@pytest.mark.anyio
async def test_delete_nonexistent_id(client: AsyncClient):
    response = await client.delete("/results/delete/nonexistent_id")
    assert response.status_code == 404
    assert response.json()["code"] == 404
    assert response.json()["status"] == "Not Found"
    assert response.json()["message"] == "Data not found"

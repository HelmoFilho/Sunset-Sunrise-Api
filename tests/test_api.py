## -- Importing External Modules -- ##
from fastapi.testclient import TestClient

## -- Importing Internal Modules -- ##
from src.main import app

client = TestClient(app)

def test_basic():

    body = {
        "type": "sunset",
        "latitude": -23.5653114,
        "longitude": -46.642659
    }
    response = client.post("api/v1/sunset-sunrise", json = body)

    assert response.status_code == 200
    assert response.json()["data"]


def test_latitude_and_longitude_range():

    body = {
        "type": "sunset",
        "latitude": -90.000001,
        "longitude": -46.642659
    }
    response = client.post("api/v1/sunset-sunrise", json = body)

    assert response.status_code == 422
    assert response.json().get("details")

    body = {
        "type": "sunset",
        "latitude": -90,
        "longitude": 180.1
    }
    response = client.post("api/v1/sunset-sunrise", json = body)

    assert response.status_code == 422
    assert response.json().get("details")


def test_type():

    body = {
        "type": "sunset",
        "latitude": -90,
        "longitude": 180
    }
    response = client.post("api/v1/sunset-sunrise", json = body)

    assert response.status_code == 200

    body = {
        "type": "sunrise",
        "latitude": -90,
        "longitude": 180
    }
    response = client.post("api/v1/sunset-sunrise", json = body)

    assert response.status_code == 200

    body = {
        "type": "asdasdasdasdasdasda",
        "latitude": -90,
        "longitude": 180
    }
    response = client.post("api/v1/sunset-sunrise", json = body)

    assert response.status_code == 422
    assert response.json().get("details")
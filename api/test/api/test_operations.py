from starlette.testclient import TestClient

from ...app.main import app

client = TestClient(app)


def test_test():
    response = client.get("/")
    assert response.status_code == 404


def test_operation_valid():
    valid_test_operation = {
        "number1": 5,
        "number2": 5
    }
    response = client.post(app.url_path_for("operation:calc"), json=valid_test_operation)
    assert response.status_code == 200
    assert response.json() == {"result": 10}

def test_operation_invalid():
    invalid_test_operation = {
        "number1": 5,
    }
    response = client.post(app.url_path_for("operation:calc"), json=invalid_test_operation)
    assert response.status_code == 422
    j = response.json()
    assert j['errors'][0]['msg'] == 'field required'

    invalid_test_operation = {
        "number1": 0,
        "number2": 5
    }
    response = client.post(app.url_path_for("operation:calc"), json=invalid_test_operation)
    assert response.status_code == 422
    j = response.json()
    assert j['errors'][0]['msg'] == 'number1 must be a positive integer'

    invalid_test_operation = {
        "number1": 5,
        "number2": -1
    }
    response = client.post(app.url_path_for("operation:calc"), json=invalid_test_operation)
    assert response.status_code == 422
    j = response.json()
    assert j['errors'][0]['msg'] == 'number2 must be a non-negative integer'

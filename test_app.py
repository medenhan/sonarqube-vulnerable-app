# test_app.py
from app import app as flask_app
import pytest

@pytest.fixture()
def app():
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app

@pytest.fixture()
def client(app):
    return app.test_client()

def test_homepage(client):
    """
    Tests if the homepage returns a successful response and contains the expected text.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_ping(client):
    response = client.get("/ping")
    assert response.status_code == 200
    assert b"pong" in response.data

import pytest

from app import create_app

@pytest.fixture
def app():
    return create_app({
        'TESTING': True,
        'OW_ENDPOINT_URL': 'http://api.openweathermap.org/data/2.5/weather?APPID=8cb95285a2549c48dfc603cb7bf9e81d'
    })

@pytest.fixture
def client(app):
    return app.test_client()

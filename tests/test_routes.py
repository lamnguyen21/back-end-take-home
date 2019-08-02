import os
import pytest

from flaskr import create_app 

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create the app with common test config
    path_prefix = os.path.join(os.path.dirname(__file__), '..')
    app = create_app({
        'TESTING': True,
        'ROUTES': path_prefix+'/data/test/routes.csv',
        'AIRPORTS': path_prefix+'/data/test/airports.csv',
    })

    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_invalid_origin(app, client):
    response = client.get('/routes/a/to/YVR').get_json()
    assert response['error'] == 'a is not a valid origin'

def test_invalid_destination(app, client):
    response = client.get('/routes/YVR/to/a').get_json()
    assert response['error'] == 'a is not a valid destination'

def test_route_not_found(app, client):
    response = client.get('/routes/ORD/to/YVR').get_json()
    assert response['error'] == 'route not found'

def test_shortest_route(app, client):
    response = client.get('/routes/YVR/to/LAX').get_json()
    assert response['route'] == ['YVR', 'LAX']

def test_shortest_route_2_hops(app, client):
    response = client.get('/routes/YYZ/to/LAX').get_json()
    assert response['route'] == ['YYZ', 'JFK', 'LAX']

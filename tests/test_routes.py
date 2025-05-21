import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'LinkedIn Post Generator' in response.data

def test_generate_post_json(client):
    response = client.post('/generate_post', json={'topic': 'AI'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'linkedin_post' in json_data

def test_generate_post_missing_topic(client):
    response = client.post('/generate_post', json={})
    assert response.status_code == 400
    json_data = response.get_json()
    assert 'error' in json_data


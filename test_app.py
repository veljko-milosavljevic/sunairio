import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_add_happy_path(client):
    response = client.get('/add?left=5&right=3')
    assert response.status_code == 200
    assert response.json == {'sum': 8}


def test_add_negative_numbers(client):
    response = client.get('/add?left=-10&right=4')
    assert response.status_code == 200
    assert response.json == {'sum': -6}


def test_missing_parameter(client):
    response = client.get('/add?left=7')
    assert response.status_code == 400
    assert 'Missing required parameters' in response.json['error']


def test_invalid_integer(client):
    response = client.get('/add?left=5&right=abc')
    assert response.status_code == 400
    assert 'must be valid integers' in response.json['error']


def test_too_many_parameters(client):
    # simuliramo >50 parametara
    params = '&'.join([f'p{i}=1' for i in range(55)])
    response = client.get(f'/add?left=1&right=2&{params}')
    assert response.status_code == 400
    assert 'Too many query parameters' in response.json['error']

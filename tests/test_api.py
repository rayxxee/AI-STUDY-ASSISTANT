import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    """Test that the /health endpoint returns 200 OK."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "ok"}

def test_query_missing_question(client):
    """Test that /query returns 400 when question is missing."""
    response = client.post('/query', json={"wrong_key": "What is AI?"})
    assert response.status_code == 400
    assert "error" in response.json

import pytest
from my_flask_app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_list_all(client):
    # Assuming you have a route '/items' that lists all items
    response = client.get('/items')
    assert response.status_code == 200
    assert 'item1' in response.get_data(as_text=True)
    assert 'item2' in response.get_data(as_text=True)
    # More assertions based on expected output

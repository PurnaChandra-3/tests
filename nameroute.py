import pytest
from my_flask_app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Optional: add sample data to the database
            db.session.add(Item(name='item1'))
            db.session.add(Item(name='item2'))
            db.session.commit()
        yield client

def test_list_by_name(client):
    # Assuming you have a route '/items/name/<name>' that lists an item by name
    response = client.get('/items/name/item1')
    assert response.status_code == 200
    assert 'item1' in response.get_data(as_text=True)
    assert 'item2' not in response.get_data(as_text=True)

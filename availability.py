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
            db.session.add(Item(name='item1', available=True))
            db.session.add(Item(name='item2', available=False))
            db.session.commit()
        yield client

def test_list_by_availability(client):
    # Assuming you have a route '/items/availability/<available>' that lists items by availability
    response = client.get('/items/availability/true')
    assert response.status_code == 200
    assert 'item1' in response.get_data(as_text=True)
    assert 'item2' not in response.get_data(as_text=True)

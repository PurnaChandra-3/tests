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
            db.session.add(Item(name='item1', category='category1'))
            db.session.add(Item(name='item2', category='category2'))
            db.session.commit()
        yield client

def test_list_by_category(client):
    # Assuming you have a route '/items/category/<category>' that lists items by category
    response = client.get('/items/category/category1')
    assert response.status_code == 200
    assert 'item1' in response.get_data(as_text=True)
    assert 'item2' not in response.get_data(as_text=True)

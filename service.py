from flask import Flask, request, jsonify, abort
from my_flask_app.models import Item, db

app = Flask(__name__)

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get(item_id)
    if item is None:
        abort(404)  # Not found

    data = request.get_json()
    if 'name' in data:
        item.name = data['name']
    if 'available' in data:
        item.available = data['available']
    
    db.session.commit()
    return jsonify(item.to_dict())  # Assuming you have a method to convert item to a dict

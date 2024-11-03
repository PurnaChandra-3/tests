from flask import Flask, jsonify, abort
from my_flask_app.models import Item, db

app = Flask(__name__)

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if item is None:
        abort(404)  # Not found

    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully'}), 204  # No Content

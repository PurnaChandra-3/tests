from flask import Flask, jsonify, abort
from my_flask_app.models import Item, db

app = Flask(__name__)

@app.route('/items/<int:item_id>', methods=['GET'])
def read_item(item_id):
    item = Item.query.get(item_id)
    if item is None:
        abort(404)  # Not found
    return jsonify(item.to_dict())  # Assuming you have a method to convert item to a dict

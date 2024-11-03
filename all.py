from flask import Flask, jsonify, abort
from my_flask_app.models import Item, db

app = Flask(__name__)

# LIST ALL function
@app.route('/items', methods=['GET'])
def list_all_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])  # Assuming you have a method to convert item to a dict

# LIST BY NAME function
@app.route('/items/name/<string:name>', methods=['GET'])
def list_by_name(name):
    item = Item.query.filter_by(name=name).first()
    if item is None:
        abort(404)  # Not found
    return jsonify(item.to_dict())

# LIST BY CATEGORY function
@app.route('/items/category/<string:category>', methods=['GET'])
def list_by_category(category):
    items = Item.query.filter_by(category=category).all()
    return jsonify([item.to_dict() for item in items])

# LIST BY AVAILABILITY function
@app.route('/items/availability/<bool:available>', methods=['GET'])
def list_by_availability(available):
    items = Item.query.filter_by(available=available).all()
    return jsonify([item.to_dict() for item in items])

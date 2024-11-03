import json
from my_flask_app.models import db, Product

def load_products():
    with open('data/products.json') as f:
        products = json.load(f)
        
    for product_data in products:
        product = Product(**product_data)  # Assuming product_data is a dict that matches Product fields
        db.session.add(product)

    db.session.commit()
    print("Products loaded successfully.")

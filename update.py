import unittest
from models import Product  # Assuming your Product model is in models.py

class TestProductModel(unittest.TestCase):
    
    def setUp(self):
        self.product = Product(id=1, name="Old Product Name", price=29.99)
    
    def test_update_product(self):
        # Update product attributes
        self.product.name = "New Product Name"
        self.product.price = 19.99
        self.product.save()  # Assuming there's a save method to update the product

        # Verify the product was updated
        updated_product = Product.get(id=1)  # Fetch the product again
        self.assertEqual(updated_product.name, "New Product Name")
        self.assertEqual(updated_product.price, 19.99)

if __name__ == '__main__':
    unittest.main()

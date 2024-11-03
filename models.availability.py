from django.test import TestCase
from myapp.models import Product

class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create Product instances with varying stock values
        Product.objects.create(name="Available Product", description="In stock", price=29.99, stock=10)
        Product.objects.create(name="Unavailable Product", description="Out of stock", price=49.99, stock=0)

    def test_find_available_products(self):
        # Retrieve available products (stock > 0)
        available_products = Product.objects.filter(stock__gt=0)

        # Check that the correct number of available products is returned
        self.assertEqual(available_products.count(), 1)

        # Optionally check the content of the available products
        product_names = [product.name for product in available_products]
        self.assertIn("Available Product", product_names)
        self.assertNotIn("Unavailable Product", product_names)

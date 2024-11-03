from django.test import TestCase
from myapp.models import Product

class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a Product instance with a specific name
        cls.product = Product.objects.create(
            name="Unique Product",
            description="A unique product description",
            price=49.99,
            stock=15
        )

    def test_find_product_by_name(self):
        # Retrieve the product by name
        product = Product.objects.get(name="Unique Product")
        
        # Verify that the retrieved product matches the expected product
        self.assertEqual(product.description, "A unique product description")
        self.assertEqual(product.price, 49.99)
        self.assertEqual(product.stock, 15)

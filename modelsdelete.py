from django.test import TestCase
from myapp.models import Product

class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up a Product instance to use in the tests
        cls.product = Product.objects.create(
            name="Sample Product",
            description="A sample product description",
            price=29.99,
            stock=50
        )

    def test_delete_product(self):
        # Delete the product
        product_id = self.product.id
        self.product.delete()

        # Check that the product no longer exists in the database
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=product_id)

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from myapp.models import Product

class ProductAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a Product instance to test the update functionality
        cls.product = Product.objects.create(
            name="Sample Product",
            description="A sample product description",
            price=29.99,
            stock=50
        )

    def test_update_product(self):
        # Update the product's details
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        data = {
            'name': 'Updated Product',
            'description': 'An updated product description',
            'price': 39.99,
            'stock': 30
        }
        response = self.client.put(url, data, format='json')

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Retrieve the updated product from the database
        self.product.refresh_from_db()

        # Check that the product's attributes have been updated
        self.assertEqual(self.product.name, 'Updated Product')
        self.assertEqual(self.product.description, 'An updated product description')
        self.assertEqual(self.product.price, 39.99)
        self.assertEqual(self.product.stock, 30)

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from myapp.models import Product

class ProductAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a Product instance to test the read functionality
        cls.product = Product.objects.create(
            name="Sample Product",
            description="A sample product description",
            price=29.99,
            stock=50
        )

    def test_read_product(self):
        # Retrieve the product using its ID
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        response = self.client.get(url)

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response data matches the expected data
        self.assertEqual(response.data['name'], self.product.name)
        self.assertEqual(response.data['description'], self.product.description)
        self.assertEqual(response.data['price'], self.product.price)
        self.assertEqual(response.data['stock'], self.product.stock)

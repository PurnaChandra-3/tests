from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from myapp.models import Product

class ProductAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a Product instance to test the delete functionality
        cls.product = Product.objects.create(
            name="Sample Product",
            description="A sample product description",
            price=29.99,
            stock=50
        )

    def test_delete_product(self):
        # Delete the product
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        response = self.client.delete(url)

        # Check that the response status code is 204 No Content
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check that the product no longer exists in the database
        self.assertFalse(Product.objects.filter(pk=self.product.pk).exists())

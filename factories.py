import factory
from myapp.models import Product

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    description = factory.Faker('sentence')
    price = factory.Faker('random_number', digits=2)
    stock = factory.Faker('random_int', min=0, max=100)

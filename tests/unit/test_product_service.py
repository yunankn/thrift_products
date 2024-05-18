from app.services.products_service import ProductsService
from app.repositories.products_repo import ProductsRepo
from app.models.product import Product

import uuid
from unittest.mock import Mock


def test_product_service():
    repo = Mock(spec=ProductsRepo)
    service = ProductsService(repo)

    product = Product(id=str(uuid.uuid4()), title='Product 1', description='Desc 1', price=250)

    repo.create_product.return_value = product
    created_product = service.create_product(product)

    repo.get_products.return_value = [created_product]
    products = service.get_products()

    assert len(products) == 1
    assert products[0].id == product.id
    assert products[0].title == product.title
    assert products[0].description == product.description
    assert products[0].price == product.price

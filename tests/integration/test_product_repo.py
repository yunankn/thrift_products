from app.models.product import Product
from app.repositories.products_repo import ProductsRepo
import uuid


def test_product_repo():
    repo = ProductsRepo()
    products = repo.get_products()
    assert isinstance(products, list)

    product = repo.create_product(
        Product(id=str(uuid.uuid4()), title='Sample Product', description='Sample Desc', price=100))

    assert isinstance(product.id, uuid.UUID)
    assert product.title == 'Sample Product'
    assert product.description == 'Sample Desc'
    assert product.price == 100

from app.models.product import Product
from app.models.comment import Comment
import uuid


def test_product_model():
    product = Product(id=str(uuid.uuid4()), title='Sample Product', description='Desc', price=500)
    assert isinstance(product.id, uuid.UUID)
    assert product.title == 'Sample Product'
    assert product.description == 'Desc'
    assert product.price == 500


def test_comment_model():
    comment = Comment(id=str(uuid.uuid4()), product_id=str(uuid.uuid4()), text='Comment Text Sample', rating=1000)
    assert isinstance(comment.id, uuid.UUID)
    assert isinstance(comment.product_id, uuid.UUID)
    assert comment.text == 'Comment Text Sample'
    assert comment.rating == 1000

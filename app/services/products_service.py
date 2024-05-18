from uuid import UUID, uuid4

from fastapi import Depends
from app.models.product import Product
from app.models.comment import Comment

from app.repositories.products_repo import ProductsRepo


class ProductsService:
    products_repo: ProductsRepo

    def __init__(self, products_repo: ProductsRepo = Depends(ProductsRepo)):
        self.products_repo = products_repo

    def get_products(self) -> list[Product]:
        return self.products_repo.get_products()

    def create_product(self, product: Product) -> Product:
        return self.products_repo.create_product(product)

    def get_comments(self, product_id: UUID) -> list[Comment]:
        return self.products_repo.get_comments(product_id)

    def create_comment(self, product_id: UUID, text: str):
        comment = Comment(id=uuid4(), product_id=product_id, text=text, rating=0)
        self.products_repo.create_comment(comment)

    def update_comment_rating(self, comment_id: UUID, delta: int):
        print(f"Update cmnt rating {comment_id} {delta}")
        self.products_repo.update_comment_rating(comment_id, delta)

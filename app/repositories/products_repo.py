from sqlalchemy.orm import Session
from uuid import UUID, uuid4

from app.database import get_db
from app.models.product import Product
from app.models.comment import Comment
from app.schemas.product import Product as DBProduct
from app.schemas.comment import Comment as DBComment

class ProductsRepo:
    db: Session

    def __init__(self):
        self.db = next(get_db())

    def __map_to_model(self, product: DBProduct) -> Product:
        return Product.model_validate(product, strict=False)

    def __map_to_scheme(self, product: Product) -> DBProduct:
        data = dict(product)
        return DBProduct(**data)

    def __map_comment_to_model(self, comment: DBComment) -> Comment:
        return Comment.model_validate(comment, strict=False)

    def __map_comment_to_scheme(self, comment: Comment) -> DBComment:
        data = dict(comment)
        return DBComment(**data)

    def get_products(self) -> list[Product]:
        return [self.__map_to_model(p) for p in self.db.query(DBProduct).all()]

    def create_product(self, product: Product) -> Product:
        try:
            db_product = self.__map_to_scheme(product)
            self.db.add(db_product)
            self.db.commit()
            return self.__map_to_model(db_product)
        except:
            raise KeyError

    def create_comment(self, comment: Comment) -> Comment:
        try:
            db_comment = self.__map_comment_to_scheme(comment)
            self.db.add(db_comment)
            self.db.commit()
            return self.__map_comment_to_model(db_comment)
        except:
            raise KeyError

    def get_comments(self, product_id: UUID) -> list[Comment]:
        try:
            db_comments = self.db.query(DBComment).filter(DBComment.product_id == product_id).all()
            return [self.__map_comment_to_model(c) for c in db_comments]
        except:
            raise KeyError

    def update_comment_rating(self, comment_id: UUID, delta: int):
        try:
            db_comment = self.db.query(DBComment).filter(DBComment.id == comment_id).first()
            db_comment.rating += delta
            self.db.commit()
        except:
            raise KeyError

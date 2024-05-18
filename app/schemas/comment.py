from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.schemas.base_schema import Base


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    product_id = Column(UUID(as_uuid=True))
    text = Column(String)
    rating = Column(Integer)

from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.schemas.base_schema import Base


class Product(Base):
    __tablename__ = 'product'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    price = Column(Integer)

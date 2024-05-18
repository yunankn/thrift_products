from uuid import UUID
from typing_extensions import Annotated
from pydantic import BaseModel, Field, ConfigDict


class Product(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    title: str
    description: str
    price: int

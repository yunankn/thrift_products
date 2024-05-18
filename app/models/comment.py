from uuid import UUID
from pydantic import BaseModel, ConfigDict


class Comment(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    product_id: UUID
    text: str
    rating: int

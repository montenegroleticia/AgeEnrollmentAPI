from pydantic import BaseModel, Field
from typing import Optional

class AgeGroup(BaseModel):
    id: Optional[str] = Field(alias="_id")
    min_age: int
    max_age: int

from pydantic import BaseModel, Field
from typing import Optional

class Enrollment(BaseModel):
    id: Optional[str] = Field(alias="_id")
    name: str
    age: int
    cpf: str
    status: str = "pending"

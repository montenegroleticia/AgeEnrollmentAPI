from pydantic import BaseModel

class AgeGroupCreate(BaseModel):
    min_age: int
    max_age: int

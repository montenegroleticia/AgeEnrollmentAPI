from pydantic import BaseModel

class EnrollmentCreate(BaseModel):
    name: str
    age: int
    cpf: str

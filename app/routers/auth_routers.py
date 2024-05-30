from fastapi import APIRouter, Depends
from app.auth.auth import get_current_username

auth_router = APIRouter()

@auth_router.get("/")
def read_current_user(username: str = Depends(get_current_username)):
    return {"username": username}

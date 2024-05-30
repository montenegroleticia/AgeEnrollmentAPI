from fastapi import FastAPI, Depends
from app.auth.auth import get_current_username
from .routers.auth_routers import auth_router
from .routers.age_group_router import age_groups_router
from .routers.enrollments_router import enrollments_router

app = FastAPI()

app.include_router(auth_router, prefix="/users/me", tags=["users"])
app.include_router(age_groups_router, prefix="/age-groups", tags=["age-groups"], dependencies=[Depends(get_current_username)])
app.include_router(enrollments_router, prefix="/enrollments", tags=["enrollments"], dependencies=[Depends(get_current_username)])

@app.get("/")
def read_root():
    return {"Hello": "World"}

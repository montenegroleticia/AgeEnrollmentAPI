from fastapi import FastAPI
from .routers.age_group_router import age_groups_router

app = FastAPI()

app.include_router(age_groups_router, prefix="/age-groups", tags=["age-groups"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

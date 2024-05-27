from fastapi import FastAPI
from .controllers.age_group_controller import age_groups_router

app = FastAPI()

app.include_router(age_groups_router, prefix="/age-groups", tags=["age-groups"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

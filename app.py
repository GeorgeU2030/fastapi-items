from fastapi import FastAPI
from routes.items import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"Hello Items"}
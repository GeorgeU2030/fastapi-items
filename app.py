from fastapi import FastAPI
from routes.items import router

# initialize FastAPI app
app = FastAPI()

# include the items router
app.include_router(router)

# main route with a simple message -GET request
@app.get("/")
def read_root():
    return {"Items"}
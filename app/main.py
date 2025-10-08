from fastapi import FastAPI
from app.routers import todos

app = FastAPI()

app.include_router(todos.router)

@app.get("/")
def index():
    return { "message": "Root path" }

@app.post("/token")
def generate_token():
    return { "token": "foo" }


from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Docker CI/CD Demo",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Hello from Docker CI/CD!"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}
from fastapi import FastAPI
from .database import sessionLocal, engine

app = FastAPI()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def index():
    return {"Hello": "World"}

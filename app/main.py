from fastapi import FastAPI
from .database import sessionLocal, engine
from . import models
from .models import Teacher

app = FastAPI()

# models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)


# Database dependency
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def index():
    return {"Hello": "World"}


@app.get("/teachers")
async def all_teachers():
    db = get_db()
    all = db.query(Teacher).all()
    return {"Successful": all}

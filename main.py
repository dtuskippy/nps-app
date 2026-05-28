from fastapi import FastAPI
from database import engine
from models import Base
from routers import parks, favorites


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(parks.router)
app.include_router(favorites.router)

@app.get("/")
def root():
    return {"message": "NPS-App Proof of Life!"}


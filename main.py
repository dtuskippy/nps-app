from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "NPS-App Proof of Life!"}
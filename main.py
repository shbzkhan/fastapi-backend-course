from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello world form FastAPI VENV"}
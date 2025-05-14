from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def first():
    return {"message": "Hello World"}

@app.get("/first")
def first():
    return {"message": "learning fastapi"}


from fastapi import FastAPI
import json

app = FastAPI()
def read_json():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/")
def first():
    return {"message": "Hello World"}

@app.get("/first")
def secand():
    return {"message": "learning fastapi"}

@app.get("/view")
def view():
    return {"message": read_json()} 
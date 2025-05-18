from fastapi import FastAPI   #uvicorn app:app --reload
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
    data = read_json()
    return data 
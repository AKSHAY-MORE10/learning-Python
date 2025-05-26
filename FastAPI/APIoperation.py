from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel      
import json

app = FastAPI()

class Patient(BaseModel):
    id = int
    name = str
    age = int
    gender = str
    blood_type = str
    conditions = list
    admitted = bool


def read_json():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


@app.get("/view")
def view():
    data = read_json()
    return data


@app.get("/view/{id}")
def view(id: int = Path(..., description="Enter Patient ID", example=1)):
    data = read_json()

    for i in data:
        if i["id"] == id:
            return i
        raise HTTPException(status_code=404, detail="Patient not found")
    return { "message": "Patient not found"}


@app.get("/sorted")
def sorted_data(
    sort_by: str = Query(..., description = "extract no the basis of admited", example = "true"),
    order: str = Query('asc', description = "sort in asc and desc order")
):
    valid_fields = ['admitted']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail = "Invalid field")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail = "Invalid order")
    
    data = read_json()
    sorted_data = sorted(data, key=lambda x:(x[sort_by], x["age"]), reverse=(order == "desc"))
    return sorted_data

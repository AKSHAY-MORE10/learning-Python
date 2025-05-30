from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel      
import json
from typing import List, Dict
import os

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



@app.get("/total_admitted")
def total_admitted():
    """
    Return the total number of admitted patients.
    
    This endpoint will return the total number of patients who have been admitted.
    """
    data = read_json()
    
    # Count the number of patients who have been admitted
    count = 0
    for i in data:
        if i["admitted"] == True:
            count += 1

    return {"total_admitted": count}




# append patient
@app.post("/append")
def append(patient: Patient):
    data = read_json()
    data.append(patient.dict())

    with open("patients.json", "w") as f:
        json.dump(data, f)
    return patient

# update patient
@app.put("/update/{id}")
def update(id : int, patient: Patient):
    data = read_json()
    for i in data:
        if i["id"] == id:
            i["name"] = patient.name
            i["age"] = patient.age
            i["gender"] = patient.gender
            i["blood_type"] = patient.blood_type
            i["conditions"] = patient.conditions
            i["admitted"] = patient.admitted
            break
    with open("patients.json", "w") as f:
        json.dump(data, f)
    return patient


@app.put("updates/{id}")
def updates(id :int , conditions: list = Query(None), admitted: bool = Query(None)):
    data = read_json()
    for i in data:
        if i["id"] == id:
            i[conditions] = conditions
            i[admitted] = admitted
            break

    with open("patients.json", "w") as f:
        json.dump(data, f)
    return data


@app.delete("/delete/{id}")
def delete_patient(id: int):
    data = read_json()
    new_data = [i for i in data if i["id"] != id]
    if len(new_data) == len(data):
        raise HTTPException(status_code=404, detail="Patient not found")
    with open("patients.json", "w") as f:
        json.dump(new_data, f)
    return {"message": "Patient deleted successfully"}


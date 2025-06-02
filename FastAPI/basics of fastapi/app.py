from fastapi import FastAPI, Path, HTTPException, Query
from typing import Optional, List
from pydantic import BaseModel
import json
import os

app = FastAPI()


# Pydantic Model for Patient

class Patient(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    blood_type: Optional[str] = None
    conditions: Optional[List[str]] = None
    admitted: Optional[bool] = None


# Utility Function to Read JSON

def read_json():
    if not os.path.exists("patients.json"):
        with open("patients.json", "w") as f:
            json.dump([], f)
    with open("patients.json", "r") as f:
        return json.load(f)


# Total Admitted Endpoint

@app.get("/total_admitted")
def total_admitted():
    data = read_json()
    count = sum(1 for i in data if i.get("admitted") is True)
    return {"total_admitted": count}


# Append New Patient

# @app.post("/append")
# def append(patient: Patient):
#     data = read_json()
#     new_id = max([i.get("id", 0) for i in data], default=0) + 1
#     patient_dict = patient.dict()
#     patient_dict["id"] = new_id
#     data.append(patient_dict)
#     with open("patients.json", "w") as f:
#         json.dump(data, f, indent=4)
#     return patient_dict


@app.post("/append")
def append(patient:Patient):
    data = read_json()
    for p in data:
        if p["id"] == patient.id:
            raise HTTPException(status_code=409, detail="Patient already exists")
        data.appent(patient.dict())
        with open ("patients.json", "w") as f:
            json.dump(data, f, indent=4)
            return data




# Update Entire Patient by ID
@app.put("/update/{id}")
def update(id: int, patient: Patient):
    data = read_json()
    updated = False
    for i in data:
        if i.get("id") == id:
            i["name"] = patient.name
            i["age"] = patient.age
            i["gender"] = patient.gender
            i["blood_type"] = patient.blood_type
            i["conditions"] = patient.conditions
            i["admitted"] = patient.admitted
            updated = True
            break
    if not updated:
        raise HTTPException(status_code=404, detail="Patient not found")
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=4)
    return {"message": "Patient updated successfully"}





# Partial Update: Conditions & Admitted

@app.put("/updates/{id}")
def updates(
    id: int,
    conditions: Optional[List[str]] = Query(None),
    admitted: Optional[bool] = Query(None)
):
    data = read_json()
    updated = False
    for i in data:
        if i.get("id") == id:
            if conditions is not None:
                i["conditions"] = conditions
            if admitted is not None:
                i["admitted"] = admitted
            updated = True
            break
    if not updated:
        raise HTTPException(status_code=404, detail="Patient not found")
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=4)
    return {"message": "Patient partially updated successfully"}


# Delete Patient by ID
@app.delete("/delete/{id}")
def delete_patient(id: int):
    data = read_json()
    new_data = [i for i in data if i.get("id") != id]
    if len(new_data) == len(data):
        raise HTTPException(status_code=404, detail="Patient not found")
    with open("patients.json", "w") as f:
        json.dump(new_data, f, indent=4)
    return {"message": "Patient deleted successfully"}




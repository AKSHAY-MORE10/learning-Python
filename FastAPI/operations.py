from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def read_json():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

# Optional: Get data by patient ID
@app.get("/views/{id}")
def views(id: int = Path(..., description="Enter Patient ID", example=1)):
    data = read_json()
    for i in data:
        if i["id"] == id:
            return i
    raise HTTPException(status_code=404, detail="Patient not found")



@app.get("/sorted")
def sorted_data(
    sort_by: str = Query(..., description="Sort on the basis of 'blood_type' or 'age'", example="blood_type"),
    order: str = Query('asc', description="Sort order: 'asc' or 'desc'")
):
    valid_fields = ["blood_type", "age"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail="Invalid sort field")

    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid sort order")

    data = read_json()
    sorted_result = sorted(data, key=lambda x: (x[sort_by], x["age"]), reverse=(order == "desc"))

    return sorted_result



@app.get("/total_patients")
def total_patients():
    data = read_json()
    return len(data)

@app.get("/total_admitted")
def total_admitted():
    data = read_json()
    
    count = 0
    for i in data:
        if i["admitted"] == True:
            count += 1
    
    return count

from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel
import json
import os

app = FastAPI()

DATA_FILE = "patients.json"

def read_json():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def write_json(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# --------------------------
# 📌 Data Model for Patients
# --------------------------
class Patient(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    blood_type: str
    conditions: list
    admitted: bool

# --------------------------
# ✅ Create Patient
# --------------------------
@app.post("/patients")
def add_patient(patient: Patient):
    data = read_json()
    for p in data:
        if p["id"] == patient.id:
            raise HTTPException(status_code=409, detail="Patient ID already exists")
    data.append(patient.dict())
    write_json(data)
    return {"message": "Patient added successfully"}

# --------------------------
# ✅ Read Patients
# --------------------------
@app.get("/patients")
def get_all_patients():
    return read_json()

@app.get("/patients/{id}")
def get_patient(id: int = Path(..., description="Patient ID")):
    data = read_json()
    for patient in data:
        if patient["id"] == id:
            return patient
    raise HTTPException(status_code=404, detail="Patient not found")

# --------------------------
# ✅ Update Condition/Status
# --------------------------
@app.put("/patients/{id}")
def update_patient(id: int, conditions: list = Query(None), admitted: bool = Query(None)):
    data = read_json()
    for patient in data:
        if patient["id"] == id:
            if conditions is not None:
                patient["conditions"] = conditions
            if admitted is not None:
                patient["admitted"] = admitted
            write_json(data)
            return {"message": "Patient updated"}
    raise HTTPException(status_code=404, detail="Patient not found")

# --------------------------
# ✅ Delete Patient by ID
# --------------------------
@app.delete("/patients/{id}")
def delete_patient(id: int):
    data = read_json()
    new_data = [p for p in data if p["id"] != id]
    if len(new_data) == len(data):
        raise HTTPException(status_code=404, detail="Patient not found")
    write_json(new_data)
    return {"message": "Patient deleted"}

# --------------------------
# ✅ Bulk Update: Discharge if age < 25
# --------------------------
@app.put("/patients/bulk-discharge")
def bulk_discharge():
    data = read_json()
    for patient in data:
        if patient["age"] < 25:
            patient["admitted"] = False
    write_json(data)
    return {"message": "All patients under age 25 discharged"}

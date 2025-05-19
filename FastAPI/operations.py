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

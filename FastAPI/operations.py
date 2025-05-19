from fastapi import FastAPI , Path , HTTPException, Query
import json

app = FastAPI

def read_json():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data



#getting data by pacient ids
@app.get("/view/{id}")
def view(id: int = Path(..., description="Enter Patient ID", example=1)):
    data = read_json()

    for i in data:
        if i["id"] == id:
            return i
        raise HTTPException(status_code=404, detail="Patient not found")
    return { "message": "Patient not found"}

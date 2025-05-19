from fastapi import FastAPI, Path, HTTPException , Query   #uvicorn app:app --reload
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

# @app.get("/view")
# def view():
#     data = read_json()
#     return data 


#using HTTPException for error handling
@app.get("/view/{id}")
def view(id: int = Path(..., description="Enter Patient ID", example=1)):
    data = read_json()

    for i in data:
        if i["id"] == id:
            return i
        raise HTTPException(status_code=404, detail="Patient not found")
    return { "message": "Patient not found"}



#using query parameter
@app.get("/search")
def search(sort_by: str = Query(..., description="sort on the basis of blood group and age", example="A+"),
           order:str = Query('asc', description="sort in asc and desc order")):
    
    valid_fields = ["blood_type", "age"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail = "Invalid field")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail = "Invalid order")
    
    data = read_json()

    sorted_data = sorted(data, key=lambda x: (x[sort_by], x["age"]), reverse=(order == "desc"))
    return sorted_data
#http://127.0.0.1:8000/search?sort_by=age&order=asc
#http://127.0.0.1:8000/search?sort_by=blood_type&order=asc




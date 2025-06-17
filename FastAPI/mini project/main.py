import os 
from fastapi import FastAPI


app = FastAPI()

@app.get("/server")

def server():
    return {"message":"hello"}



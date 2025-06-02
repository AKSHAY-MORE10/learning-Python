# FastAPI Overview 🚀

## What is FastAPI?

**FastAPI** is a modern, fast (high-performance), web framework for building APIs with **Python 3.7+** based on standard **Python type hints**. It is built on top of **Starlette** for the web parts and **Pydantic** for data validation.

---

## Why Use FastAPI in Real-World Applications?

FastAPI is widely used for building:

- **REST APIs** and **microservices**
- **Machine Learning model deployment**
- **Web applications backends**
- **IoT** and **mobile app** backends
- **Internal tooling APIs**
- **Chatbots and automation systems**

### Real-World Use Cases:

- **Netflix** uses FastAPI for some of its internal tools.
- **Microsoft** has used FastAPI for production-grade services.
- **Uber** uses FastAPI for building performant microservices.
- Developers often use FastAPI with **Docker**, **Kubernetes**, and **CI/CD** pipelines for robust deployments.

---

# FastAPI: Features & Advantages ✨

## Key Features

- **Auto Documentation** with Swagger UI (`/docs`) and ReDoc (`/redoc`)
- **Dependency Injection System** for reusability
- **Security & Authentication** support
- **Asynchronous support** using `async def` for high performance

## Advantages

✅ Super fast performance (comparable to NodeJS and Go)  
✅ Automatic validation and type checking  
✅ Developer-friendly with automatic docs  
✅ Easy to integrate with databases  
✅ Great for async and concurrent code  

---

# HTTPException in FastAPI ⚠️

## Basic Usage
```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "Item ID doesn't exist"}
        )
    return {"item": items_db[item_id]}




Code	Name	    When to Use
400	   Bad Request	Invalid client input
401	   Unauthorized	Missing/invalid authentication
403	   Forbidden	Authenticated but no permissions
404	   Not Found	Resource doesn't exist
409	   Conflict	    Duplicate resource
422	   Unprocessable  Entity	Request validation failed
500	   Internal Server Error	Unexpected server error
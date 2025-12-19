from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI(title="Simple FastAPI Tutorial")

# ============================================
# SECTION 1: Simple APIs WITHOUT Database
# ============================================

# Simple GET endpoint - No database
@app.get("/")
def read_root():
    """
    Simple GET endpoint that returns a welcome message
    """
    return {"message": "Welcome to FastAPI Tutorial!"}

# GET endpoint with path parameter
@app.get("/hello/{name}")
def say_hello(name: str):
    """
    GET endpoint with path parameter
    Example: /hello/John will return "Hello, John!"
    """
    return {"message": f"Hello, {name}!"}
    
    
class Student(BaseModel):
    name: str
    age: int
    course: str

# Simple POST endpoint - No database
@app.post("/student")
def create_student(student: Student):
    """
    POST endpoint that receives student data and returns it
    Send JSON data like: {"name": "John", "age": 20, "course": "Computer Science"}
    """
    return {
        "message": "Student data received successfully",
        "student": {
            "name": student.name,
            "age": student.age,
            "course": student.course
        }
    }

    
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

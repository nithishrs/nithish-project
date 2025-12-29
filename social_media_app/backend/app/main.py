from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, content
# SQL imports removed

app = FastAPI(title="AI Social Media Scheduler")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all for demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(content.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to AI Social Media Scheduler API"}

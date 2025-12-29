@echo off
cd backend
echo Starting FastAPI Server...
uvicorn app.main:app --reload
pause

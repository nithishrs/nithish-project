from fastapi import APIRouter, Depends, HTTPException
from .. import models, schemas, database
from ..agents.content_agent import optimization_agent
from ..agents.timing_agent import timing_agent
from ..agents.trend_agent import trend_agent
from datetime import datetime
from bson import ObjectId

router = APIRouter(
    prefix="/content",
    tags=["content"]
)

@router.post("/optimize", response_model=schemas.OptimizedResponse)
async def optimize_content(request: schemas.OptimizationRequest):
    user_id = "1" # Demo user ID
    
    # Call AI Agent
    result = optimization_agent.optimize(request.text, request.platform)
    
    # Create Draft Document
    draft = models.ContentDraft(
        user_id=user_id,
        original_text=request.text,
        target_platforms=[request.platform],
        status="optimized",
        optimized_contents=[
            {
                "platform_name": request.platform,
                "optimized_text": result.get("optimized_text", ""),
                "hashtags": result.get("hashtags", []),
                "recommendations": result.get("explanation", ""),
                "score": result.get("score", 0)
            }
        ]
    )
    
    draft_dict = draft.dict(by_alias=True, exclude={"id"})
    
    # Insert into MongoDB
    new_draft = await database.drafts_collection.insert_one(draft_dict)
    
    # We can use new_draft.inserted_id if we needed to return the Draft ID
    
    return schemas.OptimizedResponse(
        optimized_text=result.get("optimized_text", ""),
        hashtags=result.get("hashtags", []),
        score=result.get("score", 0),
        recommendations=result.get("explanation", "")
    )

@router.post("/research-timing", response_model=schemas.TimingResponse)
async def research_timing(request: schemas.TimingRequest):
    # Agents don't touch DB in this simple implementation, so this remains mostly same, just async def wrapper if preferred
    result = timing_agent.get_best_times(request.platform, request.timezone)
    return schemas.TimingResponse(
        platform=result.get("platform"),
        best_times=result.get("best_times", []),
        reasoning=result.get("reasoning", "")
    )

@router.post("/analyze-trends", response_model=schemas.TrendResponse)
async def analyze_trends(request: schemas.TrendRequest):
    result = trend_agent.analyze_trends(request.platform)
    return schemas.TrendResponse(
        platform=result.get("platform"),
        trends=result.get("trends", []),
        hashtags=result.get("hashtags", []),
        content_ideas=result.get("content_ideas", [])
    )

@router.post("/schedule")
async def schedule_post(request: schemas.ScheduleCreate):
    # Create Schedule
    schedule = models.PostingSchedule(
        draft_id=request.draft_id,
        platform_name=request.platform,
        scheduled_datetime=request.scheduled_time,
        posted=False
    )
    
    schedule_dict = schedule.dict(by_alias=True, exclude={"id"})
    
    await database.schedules_collection.insert_one(schedule_dict)
    return {"status": "success", "message": "Post scheduled successfully"}

@router.get("/schedule")
async def get_schedule():
    schedules_cursor = database.schedules_collection.find()
    schedules = await schedules_cursor.to_list(length=100)
    
    # Fix ObjectId serialization if needed, but Pydantic/FastAPI handles dicts reasonably well
    # We need to convert ObjectId to string for JSON
    for s in schedules:
        if "_id" in s:
            s["id"] = str(s["_id"])
            del s["_id"]
            
    return schedules

from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime

# User Schemas
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    timezone: Optional[str] = "UTC"

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# Content Schemas
class ContentCreate(BaseModel):
    original_text: str
    platform: str # Single platform for immediate optimization
    
class OptimizationRequest(BaseModel):
    text: str
    platform: str

class OptimizedResponse(BaseModel):
    optimized_text: str
    hashtags: List[str]
    score: int
    recommendations: str

# Research Schemas
class TimingRequest(BaseModel):
    platform: str
    timezone: str

class TimingResponse(BaseModel):
    platform: str
    best_times: List[str]
    reasoning: str

# Trend Schemas
class TrendRequest(BaseModel):
    platform: str
    category: Optional[str] = "General"

class TrendResponse(BaseModel):
    platform: str
    trends: List[str]
    hashtags: List[str]
    content_ideas: List[str]

# Schedule Schemas
class ScheduleCreate(BaseModel):
    draft_id: str
    platform: str
    scheduled_time: datetime

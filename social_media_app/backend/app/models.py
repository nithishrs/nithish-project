from pydantic import BaseModel, Field, EmailStr, ConfigDict, GetCoreSchemaHandler, GetJsonSchemaHandler
from typing import List, Optional, Dict, Any
from datetime import datetime
from bson import ObjectId
from pydantic_core import core_schema

class PyObjectId(ObjectId):
    """
    Custom ObjectId type for Pydantic V2 validation and serialization.
    """
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.union_schema([
                core_schema.is_instance_schema(ObjectId),
                core_schema.str_schema(),
            ]),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda x: str(x)
            ),
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler
    ) -> Dict[str, Any]:
        json_schema = handler(core_schema)
        json_schema.update(type="string")
        return json_schema

class MongoBaseModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )

class User(MongoBaseModel):
    username: str
    email: EmailStr
    password_hash: str
    timezone: str = "UTC"
    target_audience: Optional[Dict[str, Any]] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Platform(BaseModel):
    platform_name: str
    platform_username: str
    preferences: Optional[Dict[str, Any]] = None

class ContentDraft(MongoBaseModel):
    user_id: str # Store as string representation of ObjectId (or PyObjectId if linked)
    original_text: str
    media_path: Optional[str] = None
    target_platforms: List[str]
    status: str = "draft"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    optimized_contents: List[Dict[str, Any]] = [] 

class PostingSchedule(MongoBaseModel):
    draft_id: str
    platform_name: str
    scheduled_datetime: datetime
    posted: bool = False
    performance_notes: Optional[str] = None

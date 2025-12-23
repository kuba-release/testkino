from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ContentResponse(BaseModel):
    id: str
    title: str
    original_title: Optional[str]
    type: str
    year: Optional[int]
    description: Optional[str]
    duration_minutes: Optional[int]
    age_rating: Optional[str]
    poster_url: Optional[str]
    imdb_rating: Optional[float]
    kp_rating: Optional[float]
    
    class Config:
        from_attributes = True
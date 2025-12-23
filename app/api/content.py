from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.models.content import Content, Genre
from app.schemas.content import ContentResponse
from typing import List, Optional

router = APIRouter(prefix="/api/v1/content", tags=["content"])

@router.get("/search", response_model=List[ContentResponse])
def search_content(
    q: Optional[str] = None,
    genre: Optional[str] = None,
    year: Optional[int] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Content)
    
    if q:
        query = query.filter(Content.title.ilike(f"%{q}%"))
    if genre:
        query = query.join(Content.genres).filter(Genre.slug == genre)
    if year:
        query = query.filter(Content.year == year)
    
    return query.limit(20).all()

@router.get("/{content_id}", response_model=ContentResponse)
def get_content(content_id: str, db: Session = Depends(get_db)):
    content = db.query(Content).filter(Content.id == content_id).first()
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    return content
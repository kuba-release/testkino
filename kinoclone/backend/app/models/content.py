from sqlalchemy import Column, String, Integer, Text, DECIMAL, TIMESTAMP, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base
import uuid

class Content(Base):
    __tablename__ = "content"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(500))
    original_title = Column(String(500))
    type = Column(String(20))  # movie, series
    year = Column(Integer)
    description = Column(Text)
    duration_minutes = Column(Integer)
    age_rating = Column(String(10))
    trailer_url = Column(String(500))
    imdb_rating = Column(DECIMAL(3, 1))
    kp_rating = Column(DECIMAL(3, 1))
    poster_url = Column(String(500))
    created_at = Column(TIMESTAMP)

# Ассоциативные таблицы
genre_association = Table(
    'content_genres',
    Base.metadata,
    Column('content_id', UUID(as_uuid=True), ForeignKey('content.id')),
    Column('genre_id', UUID(as_uuid=True), ForeignKey('genres.id'))
)

class Genre(Base):
    __tablename__ = "genres"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), unique=True)
    slug = Column(String(100), unique=True)
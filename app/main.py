from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.base import Base, engine
from app.api import auth, content

# Создание таблиц
Base.metadata.create_all(bind=engine)

app = FastAPI(title="KinoClone API", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров
app.include_router(auth.router)
app.include_router(content.router)

@app.get("/")
def root():
    return {"message": "KinoClone API is running"}
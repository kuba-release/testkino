from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://user:password@db:5432/kinoclone"
    redis_url: str = "redis://redis:6379"
    elasticsearch_url: str = "http://elasticsearch:9200"
    minio_endpoint: str = "minio:9000"
    minio_access_key: str = "minioadmin"
    minio_secret_key: str = "minioadmin"
    secret_key: str = "YOUR_SECRET_KEY_HERE_CHANGE_IN_PRODUCTION"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

settings = Settings()
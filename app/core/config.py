from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    db_url: str
    

    class Config:
        env_file = ".env"

settings = Settings()

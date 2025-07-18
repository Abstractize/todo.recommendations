from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Recommendation Service"

    class Config:
        env_file = ".env"


settings = Settings()

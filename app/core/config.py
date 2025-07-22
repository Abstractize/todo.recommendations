from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Recommendation Service"
    jwt_issuer: str = ""
    jwt_audience: str = ""
    jwt_key: str = ""
    jwt_algorithm: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()

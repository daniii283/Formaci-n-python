from pydantic_settings import BaseSettings, SettingsConfigDict
from os import path

class Settings(BaseSettings):
    DB_URL: str = f"sqlite:///{path.abspath('electronica_smart.db')}"
    model_config = SettingsConfigDict(env_file="variables_de_entorno.env")

settings = Settings()

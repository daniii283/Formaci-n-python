from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_URL: str = "sqlite:///./electronica_smart.db"
    model_config = SettingsConfigDict(env_file="variables_de_entorno.env")

settings = Settings()

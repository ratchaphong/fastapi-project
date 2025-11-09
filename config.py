from pydantic_settings import BaseSettings, SettingsConfigDict  # pyright: ignore[reportMissingImports]


class Settings(BaseSettings):
    """Class สำหรับเก็บและจัดการ Environment Variables"""
    
    # ตัวอย่าง env variables (สามารถเพิ่มได้ตามต้องการ)
    app_name: str = ""
    app_version: str = ""
    debug: bool = False
    database_url: str = ""
    api_key: str = ""
    max_items: int = 0
    environment: str = ""    
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"  # Ignore extra fields that are not defined in the class (e.g., POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB)
    )


# สร้าง instance ของ Settings
settings = Settings()


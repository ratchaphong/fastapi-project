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
    # MCP Server Configuration
    # ใช้ local server ถ้าไม่มี token, ใช้ deployed server ถ้ามี token
    mcp_server_url: str = "http://localhost:8001/mcp"  # Default: local server
    mcp_bearer_token: str = ""  # Bearer token สำหรับ deployed server (ถ้ามี)
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"  # Ignore extra fields that are not defined in the class (e.g., POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB)
    )


# สร้าง instance ของ Settings
settings = Settings()


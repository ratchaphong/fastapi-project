# Schemas package
from .user import UserCreate, UserUpdate, UserResponse
from .product import ProductCreate, ProductUpdate, ProductResponse
from .mcp import (
    GreetRequest,
    CalculateRequest,
    GreetResponse,
    CalculateResponse,
    HealthResponse,
)

# Export all schemas
__all__ = [
    # User schemas
    "UserCreate",
    "UserUpdate",
    "UserResponse",
    # Product schemas
    "ProductCreate",
    "ProductUpdate",
    "ProductResponse",
    # MCP schemas
    "GreetRequest",
    "CalculateRequest",
    "GreetResponse",
    "CalculateResponse",
    "HealthResponse",
]

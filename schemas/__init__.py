# Schemas package
from .user import UserCreate, UserUpdate, UserResponse
from .product import ProductCreate, ProductUpdate, ProductResponse

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
]

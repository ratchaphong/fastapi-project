from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal


class ProductCreate(BaseModel):
    """Schema สำหรับสร้าง product ใหม่"""
    name: str
    price: Decimal
    description: Optional[str] = None


class ProductUpdate(BaseModel):
    """Schema สำหรับอัปเดตข้อมูล product"""
    name: Optional[str] = None
    price: Optional[Decimal] = None
    description: Optional[str] = None


class ProductResponse(BaseModel):
    """Schema สำหรับ response ข้อมูล product"""
    id: int
    name: str
    price: Decimal
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # อนุญาตให้แปลงจาก ORM model เป็น Pydantic model


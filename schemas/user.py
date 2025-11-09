from pydantic import BaseModel, EmailStr, field_serializer
from typing import Optional
from datetime import datetime
from decimal import Decimal


class UserCreate(BaseModel):
    """Schema สำหรับสร้าง user ใหม่"""
    name: str
    email: EmailStr
    age: Optional[int] = None
    salary: Optional[float] = None  # ใช้ float แทน Decimal เพื่อหลีกเลี่ยงปัญหา serialization


class UserUpdate(BaseModel):
    """Schema สำหรับอัปเดตข้อมูล user"""
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
    salary: Optional[float] = None  # ใช้ float แทน Decimal


class UserResponse(BaseModel):
    """Schema สำหรับ response ข้อมูล user"""
    id: int
    name: str
    email: str
    age: Optional[int] = None
    salary: Optional[float] = None  # ใช้ float แทน Decimal
    created_at: datetime
    updated_at: datetime

    @field_serializer('salary')
    def serialize_salary(self, value: Optional[Decimal]) -> Optional[float]:
        """แปลง Decimal เป็น float สำหรับ JSON serialization"""
        if value is None:
            return None
        return float(value)

    class Config:
        from_attributes = True  # อนุญาตให้แปลงจาก ORM model เป็น Pydantic model



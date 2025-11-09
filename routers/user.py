from fastapi import APIRouter, HTTPException
from typing import List
from schemas import UserCreate, UserUpdate, UserResponse
from services import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[UserResponse])
async def get_all_users():
    """ดึงข้อมูล user ทั้งหมด"""
    return await UserService.get_all_users()


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    """ดึงข้อมูล user ตาม ID"""
    try:
        return await UserService.get_user_by_id(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=UserResponse)
async def create_user(user_data: UserCreate):
    """สร้าง user ใหม่"""
    try:
        return await UserService.create_user(user_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_data: UserUpdate):
    """อัปเดตข้อมูล user"""
    try:
        return await UserService.update_user(user_id, user_data)
    except ValueError as e:
        # ตรวจสอบว่าเป็น error อะไร
        if "not found" in str(e).lower():
            raise HTTPException(status_code=404, detail=str(e))
        else:
            raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    """ลบ user"""
    try:
        await UserService.delete_user(user_id)
        return {"message": "User deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


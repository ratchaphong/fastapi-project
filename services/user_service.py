from typing import List
from decimal import Decimal
from models.user import User
from schemas import UserCreate, UserUpdate


class UserService:
    """Service layer สำหรับจัดการ business logic ของ User"""
    
    @staticmethod
    async def get_all_users() -> List[User]:
        """ดึงข้อมูล user ทั้งหมด"""
        return await User.all()
    
    @staticmethod
    async def get_user_by_id(user_id: int) -> User:
        """ดึงข้อมูล user ตาม ID"""
        user = await User.get_or_none(id=user_id)
        if not user:
            raise ValueError("User not found")
        return user
    
    @staticmethod
    async def create_user(user_data: UserCreate) -> User:
        """สร้าง user ใหม่"""
        # ตรวจสอบว่า email ซ้ำหรือไม่
        existing_user = await User.get_or_none(email=user_data.email)
        if existing_user:
            raise ValueError("Email already exists")
        
        user = await User.create(
            name=user_data.name,
            email=user_data.email,
            age=user_data.age,
            salary=Decimal(str(user_data.salary)) if user_data.salary is not None else None
        )
        return user
    
    @staticmethod
    async def update_user(user_id: int, user_data: UserUpdate) -> User:
        """อัปเดตข้อมูล user"""
        user = await User.get_or_none(id=user_id)
        if not user:
            raise ValueError("User not found")
        
        # ตรวจสอบ email ซ้ำ (ถ้ามีการเปลี่ยน email)
        if user_data.email and user_data.email != user.email:
            existing_user = await User.get_or_none(email=user_data.email)
            if existing_user:
                raise ValueError("Email already exists")
        
        # อัปเดตข้อมูล
        if user_data.name is not None:
            user.name = user_data.name
        if user_data.email is not None:
            user.email = user_data.email
        if user_data.age is not None:
            user.age = user_data.age
        if user_data.salary is not None:
            user.salary = Decimal(str(user_data.salary))
        await user.save()
        return user
    
    @staticmethod
    async def delete_user(user_id: int) -> None:
        """ลบ user"""
        user = await User.get_or_none(id=user_id)
        if not user:
            raise ValueError("User not found")
        
        await user.delete()


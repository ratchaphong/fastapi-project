from fastapi import APIRouter, HTTPException
from typing import List
from schemas import ProductCreate, ProductUpdate, ProductResponse
from services import ProductService

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=List[ProductResponse])
async def get_all_products():
    """ดึงข้อมูล product ทั้งหมด"""
    return await ProductService.get_all_products()


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int):
    """ดึงข้อมูล product ตาม ID"""
    try:
        return await ProductService.get_product_by_id(product_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=ProductResponse)
async def create_product(product_data: ProductCreate):
    """สร้าง product ใหม่"""
    try:
        return await ProductService.create_product(product_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(product_id: int, product_data: ProductUpdate):
    """อัปเดตข้อมูล product"""
    try:
        return await ProductService.update_product(product_id, product_data)
    except ValueError as e:
        # ตรวจสอบว่าเป็น error อะไร
        if "not found" in str(e).lower():
            raise HTTPException(status_code=404, detail=str(e))
        else:
            raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{product_id}")
async def delete_product(product_id: int):
    """ลบ product"""
    try:
        await ProductService.delete_product(product_id)
        return {"message": "Product deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


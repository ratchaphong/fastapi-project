from typing import List
from models.product import Product
from schemas import ProductCreate, ProductUpdate


class ProductService:
    """Service layer สำหรับจัดการ business logic ของ Product"""
    
    @staticmethod
    async def get_all_products() -> List[Product]:
        """ดึงข้อมูล product ทั้งหมด"""
        return await Product.all()
    
    @staticmethod
    async def get_product_by_id(product_id: int) -> Product:
        """ดึงข้อมูล product ตาม ID"""
        product = await Product.get_or_none(id=product_id)
        if not product:
            raise ValueError("Product not found")
        return product
    
    @staticmethod
    async def create_product(product_data: ProductCreate) -> Product:
        """สร้าง product ใหม่"""
        product = await Product.create(
            name=product_data.name,
            price=product_data.price,
            description=product_data.description
        )
        return product
    
    @staticmethod
    async def update_product(product_id: int, product_data: ProductUpdate) -> Product:
        """อัปเดตข้อมูล product"""
        product = await Product.get_or_none(id=product_id)
        if not product:
            raise ValueError("Product not found")
        
        # อัปเดตข้อมูล
        if product_data.name is not None:
            product.name = product_data.name
        if product_data.price is not None:
            product.price = product_data.price
        if product_data.description is not None:
            product.description = product_data.description
        
        await product.save()
        return product
    
    @staticmethod
    async def delete_product(product_id: int) -> None:
        """ลบ product"""
        product = await Product.get_or_none(id=product_id)
        if not product:
            raise ValueError("Product not found")
        
        await product.delete()


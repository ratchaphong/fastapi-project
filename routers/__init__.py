# Routers package
from . import user, product

# สร้าง list ของ routers
routers = [user.router, product.router]

__all__ = ["routers"]

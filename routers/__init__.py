# Routers package
from . import user, product, mcp_tools

# สร้าง list ของ routers
routers = [user.router, product.router, mcp_tools.router]

__all__ = ["routers"]

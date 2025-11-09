from tortoise.models import Model # pyright: ignore[reportMissingImports]
from tortoise import fields # pyright: ignore[reportMissingImports]


class Product(Model):
    """Product Model"""
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=200)
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    description = fields.TextField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    
    class Meta:
        table = "products"


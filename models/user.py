from tortoise.models import Model # pyright: ignore[reportMissingImports]
from tortoise import fields # pyright: ignore[reportMissingImports]


class User(Model):
    """User Model"""
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100, unique=True)
    age = fields.IntField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    salary = fields.DecimalField(max_digits=10, decimal_places=2, null=True)
    
    class Meta:
        table = "users"


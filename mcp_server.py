from fastmcp import FastMCP  # pyright: ignore[reportMissingImports]
from pydantic import BaseModel, Field
from typing import Literal

# สร้าง MCP server
mcp = FastMCP("FastAPI MCP Server")

# Pydantic Models for Tool Parameters
class GreetInput(BaseModel):
    """Input model for greet tool"""
    name: str = Field(..., description="Name of the person to greet", example="John")


class CalculateInput(BaseModel):
    """Input model for calculate tool"""
    a: float = Field(..., description="First number", example=10.0)
    b: float = Field(..., description="Second number", example=5.0)
    operation: Literal["add", "subtract", "multiply", "divide"] = Field(
        default="add",
        description="Mathematical operation to perform",
        example="add"
    )


# Tool: Greet
@mcp.tool()
def greet(input: GreetInput) -> str:
    """Generate a personalized greeting message for the given name."""
    return f"Hello, {input.name}!"


# Tool: Calculate
@mcp.tool()
def calculate(input: CalculateInput) -> float:
    """Perform basic arithmetic calculations (add, subtract, multiply, divide) between two numbers."""
    if input.operation == "add":
        return input.a + input.b
    elif input.operation == "subtract":
        return input.a - input.b
    elif input.operation == "multiply":
        return input.a * input.b
    elif input.operation == "divide":
        if input.b == 0:
            return 0.0
        return input.a / input.b
    else:
        return 0.0

if __name__ == "__main__":
    # รันด้วย HTTP transport เพื่อให้เข้าถึงได้จาก remote
    # ใช้ 0.0.0.0 เพื่อให้สามารถเข้าถึงได้จาก container อื่นใน Docker
    mcp.run(transport="http", host="0.0.0.0", port=8001)
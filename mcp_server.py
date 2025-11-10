from fastmcp import FastMCP  # pyright: ignore[reportMissingImports]

# สร้าง MCP server (ตาม tutorial - version ง่ายๆ)
mcp = FastMCP("FastAPI MCP Server")

# Tool: Greet (ตาม tutorial)
@mcp.tool()
def greet(name: str) -> str:
    """Greet someone by name"""
    return f"Hello, {name}!"

# Tool: Calculate (ตัวอย่างเพิ่มเติม)
@mcp.tool()
def calculate(a: float, b: float, operation: str = "add") -> float:
    """Perform a simple calculation
    
    Args:
        a: First number
        b: Second number
        operation: Operation to perform (add, subtract, multiply, divide)
    """
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return 0.0
        return a / b
    else:
        return 0.0

if __name__ == "__main__":
    # รันด้วย HTTP transport เพื่อให้เข้าถึงได้จาก remote
    # ใช้ 0.0.0.0 เพื่อให้สามารถเข้าถึงได้จาก container อื่นใน Docker
    mcp.run(transport="http", host="0.0.0.0", port=8001)
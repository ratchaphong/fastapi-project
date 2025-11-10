from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Literal
from fastmcp import Client  # pyright: ignore[reportMissingImports]
from config import settings

router = APIRouter(prefix="/mcp", tags=["MCP Tools"])

# MCP Client - เชื่อมต่อไปที่ MCP server
# ใช้ settings จาก config.py (สามารถตั้งค่าใน .env ได้)
MCP_SERVER_URL = settings.mcp_server_url

# Request Models
class GreetRequest(BaseModel):
    name: str

class CalculateRequest(BaseModel):
    a: float
    b: float
    operation: Literal["add", "subtract", "multiply", "divide"] = "add"

@router.post("/greet")
async def greet_tool(request: GreetRequest):
    """Test MCP greet tool through Swagger UI"""
    try:
        client = Client(MCP_SERVER_URL)
        async with client:
            result = await client.call_tool("greet", {"name": request.name})
            return {
                "success": True,
                "result": result.data,
                "raw": result.content[0].text if result.content else None
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MCP Server error: {str(e)}")

@router.post("/calculate")
async def calculate_tool(request: CalculateRequest):
    """Test MCP calculate tool through Swagger UI"""
    try:
        client = Client(MCP_SERVER_URL)
        async with client:
            result = await client.call_tool("calculate", {
                "a": request.a,
                "b": request.b,
                "operation": request.operation
            })
            return {
                "success": True,
                "result": result.data,
                "operation": f"{request.a} {request.operation} {request.b}",
                "raw": result.content[0].text if result.content else None
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MCP Server error: {str(e)}")

@router.get("/health")
async def mcp_health():
    """Check if MCP server is running"""
    try:
        client = Client(MCP_SERVER_URL)
        async with client:
            # Try to list tools to check connection
            tools_result = await client.list_tools()
            # Handle both list and object with .tools attribute
            if isinstance(tools_result, list):
                tool_names = [tool.name if hasattr(tool, 'name') else str(tool) for tool in tools_result]
            elif hasattr(tools_result, 'tools'):
                tool_names = [tool.name for tool in tools_result.tools] if tools_result.tools else []
            else:
                tool_names = []
            
            return {
                "status": "connected",
                "mcp_server_url": MCP_SERVER_URL,
                "available_tools": tool_names
            }
    except Exception as e:
        return {
            "status": "disconnected",
            "error": str(e),
            "message": "Make sure MCP server is running on port 8001"
        }


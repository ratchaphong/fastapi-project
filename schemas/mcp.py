from pydantic import BaseModel, Field
from typing import Literal, Optional, List


# Request Models
class GreetRequest(BaseModel):
    """Request model for greet tool"""
    name: str = Field(..., description="Name to greet", example="John")


class CalculateRequest(BaseModel):
    """Request model for calculate tool"""
    a: float = Field(..., description="First number", example=10.0)
    b: float = Field(..., description="Second number", example=5.0)
    operation: Literal["add", "subtract", "multiply", "divide"] = Field(
        default="add",
        description="Mathematical operation to perform",
        example="add"
    )


# Response Models
class GreetResponse(BaseModel):
    """Response model for greet tool"""
    success: bool = Field(..., description="Whether the operation was successful")
    result: str = Field(..., description="Greeting message from MCP server")
    raw: Optional[str] = Field(None, description="Raw response content from MCP server")

    class Config:
        json_schema_extra = {
            "example": {
                "success": True,
                "result": "Hello, John!",
                "raw": "Hello, John!"
            }
        }


class CalculateResponse(BaseModel):
    """Response model for calculate tool"""
    success: bool = Field(..., description="Whether the operation was successful")
    result: float = Field(..., description="Calculation result from MCP server")
    operation: str = Field(..., description="Operation description (e.g., '10.0 add 5.0')")
    raw: Optional[str] = Field(None, description="Raw response content from MCP server")

    class Config:
        json_schema_extra = {
            "example": {
                "success": True,
                "result": 15.0,
                "operation": "10.0 add 5.0",
                "raw": "15.0"
            }
        }


class HealthResponse(BaseModel):
    """Response model for MCP server health check"""
    status: Literal["connected", "disconnected"] = Field(..., description="Connection status")
    mcp_server_url: str = Field(..., description="MCP server URL being used")
    available_tools: List[str] = Field(default_factory=list, description="List of available tools")
    error: Optional[str] = Field(None, description="Error message if disconnected")
    message: Optional[str] = Field(None, description="Additional message")

    class Config:
        json_schema_extra = {
            "example": {
                "status": "connected",
                "mcp_server_url": "http://localhost:8001/mcp",
                "available_tools": ["greet", "calculate"]
            }
        }


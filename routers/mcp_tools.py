from fastapi import APIRouter, HTTPException, status
from fastmcp import Client  # pyright: ignore[reportMissingImports]
from config import settings
from schemas.mcp import (
    GreetRequest,
    CalculateRequest,
    GreetResponse,
    CalculateResponse,
    HealthResponse,
)

router = APIRouter(prefix="/mcp", tags=["MCP Tools"])

# MCP Client - เชื่อมต่อไปที่ MCP server
# ใช้ settings จาก config.py (สามารถตั้งค่าใน .env ได้)
MCP_SERVER_URL = settings.mcp_server_url

@router.post(
    "/greet",
    response_model=GreetResponse,
    status_code=status.HTTP_200_OK,
    summary="Greet Tool",
    description="""
    Call the MCP greet tool to generate a greeting message.
    
    This endpoint connects to the MCP server and calls the `greet` tool with the provided name.
    
    **Features:**
    - Returns a personalized greeting message
    - Includes both structured result and raw response
    
    **Example:**
    - Input: `{"name": "John"}`
    - Output: `{"success": true, "result": "Hello, John!", "raw": "Hello, John!"}`
    """,
    response_description="Greeting message from MCP server"
)
async def greet_tool(request: GreetRequest) -> GreetResponse:
    """Test MCP greet tool through Swagger UI"""
    try:
        client = Client(MCP_SERVER_URL)
        async with client:
            result = await client.call_tool("greet", {"name": request.name})
            return GreetResponse(
                success=True,
                result=result.data if hasattr(result, 'data') else str(result),
                raw=result.content[0].text if result.content else None
            )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"MCP Server error: {str(e)}"
        )

@router.post(
    "/calculate",
    response_model=CalculateResponse,
    status_code=status.HTTP_200_OK,
    summary="Calculate Tool",
    description="""
    Call the MCP calculate tool to perform mathematical operations.
    
    This endpoint connects to the MCP server and calls the `calculate` tool with two numbers and an operation.
    
    **Supported Operations:**
    - `add`: Addition (a + b)
    - `subtract`: Subtraction (a - b)
    - `multiply`: Multiplication (a * b)
    - `divide`: Division (a / b)
    
    **Features:**
    - Supports basic arithmetic operations
    - Returns calculation result with operation description
    - Includes both structured result and raw response
    
    **Example:**
    - Input: `{"a": 10, "b": 5, "operation": "add"}`
    - Output: `{"success": true, "result": 15.0, "operation": "10.0 add 5.0", "raw": "15.0"}`
    """,
    response_description="Calculation result from MCP server"
)
async def calculate_tool(request: CalculateRequest) -> CalculateResponse:
    """Test MCP calculate tool through Swagger UI"""
    try:
        client = Client(MCP_SERVER_URL)
        async with client:
            result = await client.call_tool("calculate", {
                "a": request.a,
                "b": request.b,
                "operation": request.operation
            })
            return CalculateResponse(
                success=True,
                result=float(result.data) if hasattr(result, 'data') else float(result),
                operation=f"{request.a} {request.operation} {request.b}",
                raw=result.content[0].text if result.content else None
            )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"MCP Server error: {str(e)}"
        )

@router.get(
    "/health",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="MCP Server Health Check",
    description="""
    Check if MCP server is running and connected.
    
    This endpoint attempts to connect to the MCP server and list available tools.
    
    **Returns:**
    - `status`: Connection status ("connected" or "disconnected")
    - `mcp_server_url`: The MCP server URL being used
    - `available_tools`: List of available tools from MCP server
    - `error`: Error message if connection fails (only when disconnected)
    - `message`: Additional information message (only when disconnected)
    
    **Use Cases:**
    - Health monitoring
    - Debugging connection issues
    - Discovering available MCP tools
    
    **Note:** This endpoint will return error details if connection fails, but will still return HTTP 200.
    """,
    response_description="MCP server connection status and available tools"
)
async def mcp_health() -> HealthResponse:
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
            
            return HealthResponse(
                status="connected",
                mcp_server_url=MCP_SERVER_URL,
                available_tools=tool_names
            )
    except Exception as e:
        return HealthResponse(
            status="disconnected",
            mcp_server_url=MCP_SERVER_URL,
            available_tools=[],
            error=str(e),
            message="Make sure MCP server is running on port 8001"
        )


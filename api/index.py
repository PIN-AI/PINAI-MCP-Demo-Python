from starlette.applications import Starlette
from starlette.routing import Mount, Host
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("walkerAPI-mcp-server")

# 官方演示方法1
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
    
# 官方演示方法2
@mcp.tool()
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI given weight in kg and height in meters"""
    return weight_kg / (height_m**2)

# 挂载SSE服务器到ASGI服务器上
app = Starlette(
    routes=[
        Mount('/', app=mcp.sse_app()),
    ]
)

# 启动服务器
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3001)
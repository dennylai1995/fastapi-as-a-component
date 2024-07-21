from pydantic import BaseModel, Field

class SystemLoadingResponse(BaseModel):
    cpu_percent: float = Field(..., description="The current CPU usage percentage of server", example=10.5)
    mem_percent: float = Field(..., description="The current Memory usage percentage of server", example=30.7)
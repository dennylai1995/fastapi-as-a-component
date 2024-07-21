import psutil
from fastapi import APIRouter, HTTPException
from api.endpoints.system import _schema

def init_loading_router():
    
    LOADING_ROUTER = APIRouter()
    
    @LOADING_ROUTER.get('/system/loading',
                        response_model=_schema.SystemLoadingResponse)
    def get_system_loading():
        try:
            cpu = psutil.cpu_percent()
            mem = psutil.virtual_memory().percent
        except Exception as e:
            print(f'[/system/loading] error while getting cpu and mem usage ({e})')
            raise HTTPException(status_code=502, detail="Server got something wrong!")
        
        return _schema.SystemLoadingResponse(
            cpu_percent = cpu,
            mem_percent = mem
        )
    
    return LOADING_ROUTER
from fastapi import FastAPI
from api.endpoints.system import loading

def register_endpoints(fastapi_app: FastAPI):
    
    loading_router = loading.init_loading_router()
    
    fastapi_app.include_router(loading_router, tags=["system"])
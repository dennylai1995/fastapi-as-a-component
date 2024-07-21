import uvicorn
import contextlib
import time

from threading import Thread
from uvicorn.config import LOGGING_CONFIG
from fastapi import FastAPI

from api.endpoints.system import api as system_api

class FastAPIApp:
    def __init__(self):
        
        self.api_app = FastAPI()
        
        #resgister API routers
        system_api.register_endpoints(self.api_app)
    
class APIServer:
    def __init__(self, fastapi_obj: FastAPIApp):
        
        # Customize uvicorn logging
        LOGGING_CONFIG["formatters"]["access"][
            "fmt"] = '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'
        
        self.config = uvicorn.Config(fastapi_obj.api_app,
                                host="0.0.0.0",
                                port=0, # 0 means random port
                                # port=8080, # to use fixed port
                                log_config=LOGGING_CONFIG,
                                use_colors=True)
        
    def get_uvicorn_server(self):
        return UvicornServer(config=self.config)
        

class UvicornServer(uvicorn.Server):
    # credit: https://stackoverflow.com/questions/61577643/python-how-to-use-fastapi-and-uvicorn-run-without-blocking-the-thread
    def install_signal_handlers(self) -> None:
        pass

    @contextlib.contextmanager
    def run_in_thread(self):
        thread = Thread(target=self.run, daemon=True)
        thread.start()
        try:
            server_port = 0
            while not self.started:
                time.sleep(1e-3)
            # credit: https://github.com/encode/uvicorn/issues/761#issuecomment-1287679527
            for server in self.servers:
                for socket in server.sockets:
                    server_port = socket.getsockname()[1]
            yield server_port
        finally:
            self.should_exit = True
            thread.join()

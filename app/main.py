import time
from api.entrypoint import FastAPIApp, APIServer

def main():
    
    fast_api = FastAPIApp()
        
    server = APIServer(fast_api).get_uvicorn_server()

    with server.run_in_thread() as server_port:
        #NOTE: uvicorn server will be gracefully shutdown after exiting the with context
        try:
            print(f'[INIT] uvicorn server is running on port: {server_port}')
            
            while True:
                #TODO: replace the while loop with other blocking process here (e.g. ROS2 node)
                time.sleep(1)
                
        except KeyboardInterrupt:
            print(f'## Terminated by ctrl + C')
        finally:
            print(f'## Cleaning up')

if __name__ == '__main__':
    main()
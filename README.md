# fastapi-as-a-component
![test Coverage](./test/coverage-badge.svg)

An app template runs fastapi in a thread (as a component) with graceful uvicorn server shutdown and server port visibility in program.

### Key Features
1. uvicorn server runs on random port (fixed port is also possible)
2. programmatically get the port used by uvicorn server
3. gracefully shut down uvicorn server

### Tested Platform
- Ubuntu 20.04
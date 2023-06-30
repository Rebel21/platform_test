import uvicorn
from fastapi import FastAPI

from services.routers import router as router_services

app = FastAPI(
    title="Py platform"
)


app.include_router(router_services)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

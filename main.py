from fastapi import FastAPI

from services.routers import router as router_services

app = FastAPI(
    title="Py platform"
)

app.include_router(router_services)

from fastapi import APIRouter

from services.container_manager import ContainerManager
from services.shemas.service import ServiceRun

router = APIRouter(prefix='/services')

container_manager = ContainerManager()


@router.get('/')
async def get_services():
    return {'result': await container_manager.get_container_list()}


@router.post('/')
async def run_service(service: ServiceRun):
    return {'result': await container_manager.run_service(service)}


@router.post('/{service_id}')
async def stop_service(service_id: str):
    return {'result': await container_manager.stop_service(service_id)}


@router.get('/{service_id}')
async def get_service(service_id: str):
    return {'result': await container_manager.stop_service(service_id)}

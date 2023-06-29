from fastapi import APIRouter

from services.container_manager import ContainerManager

router = APIRouter(prefix='/services')

container_manager = ContainerManager()


@router.get('/')
def get_services():
    return {'result': container_manager.get_container_list()}

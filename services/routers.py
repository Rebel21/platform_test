from fastapi import APIRouter

from services.container_manager import ContainerManager

router = APIRouter(prefix='/services')

container_manager = ContainerManager()


@router.get('/')
def get_services():
    return {'result': container_manager.get_container_list()}


@router.post('/')
def run_service(token: str, repository_url: str, py_file: str):
    return {'result': container_manager.run_service(token, repository_url, py_file)}


@router.post('/{container_id}')
def run_service(container_id: str):
    return {'result': container_manager.stop_service(container_id)}


import logging

import docker

from services.shemas.service import ServiceRun

logging.basicConfig(level=logging.INFO)


class ContainerManager:

    def __init__(self):
        self._client = docker.from_env()

    async def get_container_list(self):
        return [
            {'name': container.name, 'short_id': container.short_id, 'status': container.status}
            for container in self._client.containers.list(all=True)]

    async def run_service(self, service: ServiceRun):
        container = self._client.containers.run('esmdev/test_platform:0.3',
                                                environment=[f'BOT_TOKEN={service.token}', f'URL={service.repository_url}',
                                                             f'EXEC_FILE={service.py_file}'], detach=True)
        return {'name': container.name, 'short_id': container.short_id, 'status': container.status}

    async def stop_service(self, short_id: str):
        container = self._client.containers.get(short_id)
        container.stop()
        return {'name': container.name, 'short_id': container.short_id, 'status': container.status}

    async def get_service_by_id(self, service_id):
        container = self._client.containers.get(service_id)
        return {'name': container.name, 'short_id': container.short_id, 'status': container.status}
import logging

import docker

logging.basicConfig(level=logging.INFO)


class ContainerManager:

    def __init__(self):
        self._client = docker.from_env()

    def get_container_list(self):
        return [
            {'name': container.name, 'short_id': container.short_id, 'status': container.status}
            for container in self._client.containers.list(all=True)]

    def run_service(self, token: str, repository_url: str, py_file: str):
        container = self._client.containers.run('esmdev/test_platform:0.3',
                                                environment=[f'BOT_TOKEN={token}', f'URL={repository_url}',
                                                             f'EXEC_FILE={py_file}'], detach=True)
        return {'name': container.name, 'short_id': container.short_id, 'status': container.status}

    def stop_service(self, short_id: str):
        container = self._client.containers.get(short_id)
        container.stop()
        return {'name': container.name, 'short_id': container.short_id, 'status': container.status}

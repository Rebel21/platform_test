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

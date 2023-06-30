from pydantic import BaseModel


class ServiceRun(BaseModel):
    token: str
    repository_url: str
    py_file: str

from enum import Enum
from typing import List

from pydantic import BaseModel, BaseSettings

__all__ = ('settings',)


class DbConnection(BaseModel):
    host: str
    port: int


class _Settings(BaseSettings):
    db_name: str = 'chat'
    db_user: str = 'chat'
    db_password: str = ''
    db_shards: List[DbConnection] = []


settings = _Settings()

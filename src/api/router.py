from fastapi import APIRouter

from src.api import chat

router = APIRouter(prefix='')

router.include_router(chat.router)

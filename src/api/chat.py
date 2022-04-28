from typing import List

from fastapi import APIRouter, status

from src.apps.chat.schema import Message, MessageOut
from src.apps.service.chat import ChatService

router = APIRouter(prefix='/chat')


@router.post('/{chat_id}/', response_model=MessageOut)
async def create_message(chat_id, message: Message):
    return await ChatService().create_message(chat_id, message)


@router.get('/{chat_id}/', response_model=List[MessageOut])
async def get_messages(chat_id: int, message_id: int = None):
    messages = await ChatService().get_messages(chat_id, message_id)
    return messages


@router.post('/{chat_id}/{message_id}')
async def read_message(chat_id: int, message_id):
    await ChatService().read_message(chat_id, message_id)
    return status.HTTP_204_NO_CONTENT

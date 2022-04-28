from datetime import datetime

from pydantic import BaseModel


class Message(BaseModel):
    user_id: int
    text: str
    # created_at: datetime # todo: get from client.


class MessageOut(Message):
    message_id: int
    chat_id: int
    user_id: int
    text: str
    created_at: datetime

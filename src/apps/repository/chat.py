from datetime import datetime, timezone
from src.apps.chat.schema import Message
from src.apps.repository.base import BaseRepository


class ChatRepository(BaseRepository):
    async def create_message(self, chat_id, message: Message):
        # FixMe: get created dt from client
        create_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
        query = """
        insert into message(chat_id, user_id, created_at, text) 
        values (%s, %s, %s, %s)
        """
        args = (
            chat_id, message.user_id, create_dt, message.text,
        )
        message_id = await self.insert_to_shard(chat_id, query, args)
        return {
            "message_id": message_id,
            "created_at": create_dt,
            "chat_id": chat_id,
            "user_id": message.user_id,
            "text": message.text,
        }

    async def get_messages(self, chat_id, from_message_id):
        query = """
            select id, chat_id, user_id, text, created_at
            from message
            where id >= %s
        """
        rows = await self.do_query_in_shard(chat_id, query, (from_message_id,))
        return [
            {
                'message_id': row[0],
                'chat_id': row[1],
                'user_id': row[2],
                'text': row[3],
                'created_at': row[4],
            }
            for row in rows
        ]
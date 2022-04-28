import asyncio

from src.database.connection import do_query, get_shard_connection, insert


class BaseRepository:

    async def do_query_in_shard(self, chat_id, query, args):
        return await do_query(
            await get_shard_connection(chat_id, asyncio.get_running_loop()),
            query, args,
        )

    async def insert_to_shard(self, chat_id, query, args):
        return await insert(
            await get_shard_connection(chat_id, asyncio.get_running_loop()),
            query, args,
        )

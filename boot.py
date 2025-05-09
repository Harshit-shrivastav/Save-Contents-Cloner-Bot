import asyncio, re
from pyrogram import Client, idle
from database import db
from config import Telegram 

async def start_client(token):
    client_name = re.sub(r'[^a-zA-Z0-9]', '', token)
    client = Client(in_memory=True, name=client_name, api_id=Telegram.API_ID, api_hash=Telegram.API_HASH, bot_token=token, plugins={"root": "plugins"})
    try:
        await client.start()
        await idle()
    except:
        pass 

async def main():
    bot_tokens = await db.fetch_all("tokens")  
    tasks = [start_client(token) for token in bot_tokens]
    await asyncio.gather(*tasks)
    print('All clients booted')

if __name__ == "__main__":
    asyncio.run(main())
